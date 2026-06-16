# AIoT Smart Recycling System

AIoT Smart Recycling System is a smart recycling solution that combines AI-based image recognition (YOLO) with IoT multi-sensors. The system automatically identifies waste types, provides recycling instructions, and monitors temperature and humidity to maintain hygiene conditions.

**Introduction to Internet of Things (IoT) – Team Project**  
**School of Computing, Gachon University | Team J**

---

## Team Members

| Name | Role |
|--------|--------|
| Yeonjeong Choi | System Design, Circuit Design, PPT |
| Jiyoon Kim | Programming, Circuit Troubleshooting (DHT22, HC-SR04), Presentation |
| Suhee Kim | Circuit Troubleshooting (LCD, Servo Motor), Notion Report, GitHub |

---

## Project Objectives

- **Sensor Fusion:** Combine YOLO-based object detection with ultrasonic and temperature/humidity sensor data.
- **Smart User Interface:** Display recycling instructions and classification results through an LCD screen.
- **Environmental Management:** Monitor temperature and humidity while automatically controlling the lid using a servo motor.

---

## System Architecture

### Waste Classification Flow

User Approaches  
→ HC-SR04 Detects Presence  
→ Camera Activated  
→ YOLO Inference (Plastic / Can / Paper)  
→ LCD Displays Classification Result  
→ Servo Motor Opens Lid

### Environmental Monitoring Flow

Idle State  
→ DHT22 Monitors Temperature and Humidity

Both processes run simultaneously using multithreading.

---

## Hardware Components

- Raspberry Pi 5
- CSI Camera
- HC-SR04 Ultrasonic Sensor
- DHT22 Temperature & Humidity Sensor
- I2C LCD 1602
- SG90 Servo Motor

---

## AI Model (YOLO)

### Base Model
- YOLOv8n (Lightweight model suitable for Raspberry Pi)

### Classes
- Plastic (PET Bottles)
- Can
- Paper

### Dataset
- Self-collected images
- Labeled using Roboflow

### Training Environment
- Google Colab (GPU)
- Fine-tuning performed on custom dataset

---

## Development Timeline

| Date | Progress |
|--------|--------|
| June 12 | Project planning and idea finalization |
| June 13 | Environment setup (Wi-Fi, YOLO, Camera) |
| June 14 | Circuit implementation and YOLO training |
| June 15 | Hardware integration and system testing |
| June 16 | Final testing and documentation |

---

## Issues & Solutions

| Issue | Solution |
|---------|---------|
| LCD connection issue | Wiring inspection and code modification |
| LCD mounting issue | Resolved using reference materials |
| Storage limitation | Adopted lightweight YOLOv8n |
| Servo motor and lid coupling issue | Direct shaft coupling through a custom hole |
| Plastic/Paper misclassification | Improved classification logic |
| Limited GPIO pins | Pin reallocation and shared power configuration |
| Ultrasonic sensor measurement failure | Circuit and code modifications |
| Insufficient bin space | Built a custom recycling bin |

---

## Future Improvements

- Improve detection accuracy with more training data
- Integrate Firebase or Google Sheets for real-time monitoring
- Support multiple-object recognition
- Add voice guidance functionality

---

## Results

### System Structure
(Add architecture image)

### Circuit Configuration
(Add circuit image)

### Object Detection Results
(Add YOLO detection screenshots)

### Final Prototype
(Add final project photos)
