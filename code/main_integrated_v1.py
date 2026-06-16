from gpiozero import DistanceSensor
from time import sleep
import os
import board
import adafruit_dht
from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2)

sensor = DistanceSensor(
    echo=24,
    trigger=23,
    max_distance=2,
    queue_len=1
)

dht = adafruit_dht.DHT11(board.D4)

while True:
    distance_cm = sensor.distance * 100
    print("Distance:", round(distance_cm, 1), "cm")

    if distance_cm < 20:
        print("CAMERA ON")

        lcd.clear()
        lcd.write_string("CAMERA ON")

        os.system("rpicam-jpeg -o image.jpg")

        lcd.clear()
        lcd.write_string("AI CHECKING")

        os.system("python3 predict2.py")

        sleep(5)

    else:
        try:
            temp = dht.temperature
            hum = dht.humidity

            lcd.clear()
            lcd.write_string(f"T:{temp}C")
            lcd.cursor_pos = (1, 0)
            lcd.write_string(f"H:{hum}%")

            print("Temp:", temp, "Hum:", hum)

        except Exception as e:
            print("DHT ERROR:", e)

            lcd.clear()
            lcd.write_string("DHT ERROR")

        sleep(2)