# 📱 Phone Detector using YOLOv8 + Sound Alert + WhatsApp Integration

This project detects mobile phones in real-time using a webcam, triggers a sound alert, saves an image of the detection, and sends a WhatsApp message with the detected photo via Twilio and Imgur.

---

## 🚀 Features

- ✅ Real-time object detection using YOLOv8
- ✅ Phone alert system using your laptop webcam
- ✅ Sound alert on detection (`alert.wav`)
- ✅ Saves snapshot of detection
- ✅ Sends WhatsApp message via Twilio
- ✅ Image uploaded automatically to Imgur for public access

---

## 📸 Live Demo
![Demo](demo.gif) <!-- Optional demo GIF or image -->

---

## 🧠 Tech Stack

| Tool         | Purpose                              |
|--------------|---------------------------------------|
| Python       | Main programming language             |
| OpenCV       | Webcam capture and image processing   |
| Ultralytics YOLOv8 | Object detection (phone recognition) |
| Pygame       | Sound alert handling                  |
| Twilio API   | WhatsApp message sending              |
| Imgur API    | Upload image to a public link         |
| .env         | Store credentials securely            |

---

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/sundram6452/mobile-detection-and-sending--alert-with-pic-on-whatsapp
cd phoneDetector
python phone_detector.py

