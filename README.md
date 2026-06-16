# AIoT Smart Recycling System

AIoT Smart Recycling System is a smart recycling solution that combines AI-based object recognition (YOLO) with IoT multi-sensors. The system automatically identifies waste types, provides recycling instructions, and monitors temperature and humidity to maintain hygiene conditions.

> Introduction to Internet of Things (IoT) Team Project  
> Team J

---

## Team Members and Roles

| Name | Role |
|--------|--------|
| Yeonjeong Choi | System Design, Circuit Design, PPT |
| Jiyoon Kim | Programming, Circuit Troubleshooting (DHT22, HC-SR04) |
| Suhee Kim | Circuit Troubleshooting (LCD, Servo Motor), Notion Report, GitHub |

---

## Project Objectives

### Sensor Fusion

Combine camera-based AI recognition (YOLO) with ultrasonic and temperature/humidity sensor data to make comprehensive decisions based on environmental conditions.

### Smart UI

Provide intuitive recycling instructions and classification results through an LCD display.

### Eco-Impact

Monitor temperature and humidity to maintain hygiene conditions and automatically control the lid using a servo motor.

---

## System Architecture

### Waste Classification Process

User Approaches  
→ HC-SR04 Ultrasonic Sensor Detects Presence  
→ Camera Activated  
→ YOLO Object Detection (Plastic / Can / Paper)  
→ Classification Result Displayed on LCD  
→ Servo Motor Opens the Lid

### Environmental Monitoring Process

DHT22 Temperature & Humidity Sensor Measures Data  
→ Temperature and Humidity Monitoring  
→ LCD Display Output

Both processes run simultaneously using multithreading.

---

## Hardware Components

| Component | Purpose |
|------------|------------|
| Raspberry Pi 5 | Central Processing Unit (Edge AI) |
| CSI Camera | Image Capture for YOLO Inference |
| HC-SR04 | User Detection |
| DHT22 | Temperature and Humidity Monitoring |
| I2C LCD 1602 | Display Classification Results and Instructions |
| SG90 Servo Motor | Automatic Lid Control |

---

## AI Model (YOLO)

### Base Model

- YOLOv8n
- Lightweight model selected for Raspberry Pi environments

### Classes

- Plastic (PET Bottles)
- Can
- Paper

### Dataset

- Self-collected images
- Labeled using Roboflow

### Training Environment

- Google Colab (GPU)
- Fine-tuning performed on a custom dataset

---

## Development Timeline

| Date | Description |
|--------|--------|
| June 12 | Project planning and idea finalization |
| June 13 | Environment setup (Wi-Fi, YOLO, Camera) |
| June 14 | Circuit implementation, sensor installation, and YOLO training |
| June 15 | Hardware integration, system testing, and YOLO integration |
| June 16 | Final inspection and documentation |

---

## Issues and Solutions

| Issue | Solution |
|--------|--------|
| LCD connection issue | Wiring inspection and code modification |
| LCD mounting issue | Resolved using reference materials |
| Storage limitation | Adopted YOLOv8n lightweight model |
| Servo motor and lid coupling issue | Drilled a hole and directly connected the servo shaft |
| Plastic/Paper misclassification | Improved classification logic |
| Limited GPIO pins | Pin reallocation and shared power configuration |
| Ultrasonic sensor distance measurement failure | Circuit and code modifications |
| Insufficient bin space | Built a custom recycling bin |

---

## Code and Results

- Source code and project results are included in this GitHub repository.

---

## Future Improvements

- Improve recognition accuracy with a larger training dataset
- Integrate Firebase or Google Sheets for real-time monitoring and visualization
- Support multiple-object recognition
- Add voice guidance functionality
