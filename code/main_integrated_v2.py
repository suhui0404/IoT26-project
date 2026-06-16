import cv2
import numpy as np
import onnxruntime as ort

from time import sleep
from RPLCD.i2c import CharLCD
from gpiozero import AngularServo

lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2)
servo = AngularServo(18)

CLASS_NAMES = ["glass", "metal", "paper", "plastic", "trash"]

img = cv2.imread("image.jpg")

img = cv2.resize(img, (640, 640))
img = img.astype(np.float32) / 255.0
img = np.transpose(img, (2, 0, 1))
img = np.expand_dims(img, axis=0)

session = ort.InferenceSession("/home/pi/best.onnx")
outputs = session.run(None, {"images": img})

pred = np.squeeze(outputs[0])
class_scores = pred[4:9, :]
max_scores = class_scores.max(axis=1)

print("Class score:")
for name, score in zip(CLASS_NAMES, max_scores):
    print(name, float(score))

if max_scores[3] > 0.10:
    class_id = 3
else:
    class_id = int(np.argmax(max_scores))

score = float(max_scores[class_id])
label = CLASS_NAMES[class_id]

print("Detected:", label)
print("Confidence:", score)

lcd.clear()
lcd.write_string(label.upper())
lcd.cursor_pos = (1, 0)
lcd.write_string("PUT INSIDE")

print("SERVO OPEN")
servo.max()
sleep(3)

print("SERVO CLOSE")
servo.min()
sleep(3)

servo.detach()