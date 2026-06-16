from gpiozero import AngularServo
from time import sleep

servo = AngularServo(18)

while True:

    print("OPEN")
    servo.max()

    sleep(3)

    print("CLOSE")
    servo.min()

    sleep(3)