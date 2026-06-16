from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(
    echo=24,
    trigger=23,
    max_distance=2,
    queue_len=1
)

while True:
    distance_cm = sensor.distance * 100

    print("Distance:", round(distance_cm, 1), "cm")

    sleep(0.5)