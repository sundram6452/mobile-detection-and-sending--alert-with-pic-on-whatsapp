from ultralytics import YOLO
import cv2
import pygame
import time
import os
from datetime import datetime
from dotenv import load_dotenv
from twilio.rest import Client

# Load env variables
load_dotenv()
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH")
from_whatsapp = os.getenv("TWILIO_FROM")
to_whatsapp = os.getenv("TWILIO_TO")
client = Client(account_sid, auth_token)

# Initialize sound
pygame.init()
pygame.mixer.init()
alert_sound = pygame.mixer.Sound("alert.wav")

# Load model
model = YOLO("runs/detect/train4/weights/best.pt")  # Update if needed

# Webcam
cap = cv2.VideoCapture(0)

# Create folder for detections
os.makedirs("detections", exist_ok=True)
last_beep_time = 0
cooldown = 10  # seconds

print("📸 Phone Detector started. ESC to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]
    phone_detected = False

    for box in results.boxes:
        cls = int(box.cls[0])
        name = model.names[cls]
        if "phone" in name.lower():
            phone_detected = True
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    if phone_detected and time.time() - last_beep_time > cooldown:
        # Save frame
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"detections/detected_{ts}.jpg"
        cv2.imwrite(filename, frame)

        # Play sound
        alert_sound.play()

        # Send WhatsApp message
        message = client.messages.create(
            body=f"📱 Phone detected at {ts}!",
            from_=from_whatsapp,
            to=to_whatsapp
        )
        print("✅ WhatsApp alert sent:", message.sid)

        last_beep_time = time.time()

    cv2.imshow("Phone Detector", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
