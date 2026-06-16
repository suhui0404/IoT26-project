import time
import board
import adafruit_dht

dht = adafruit_dht.DHT11(board.D4)

while True:
    try:
        temp = dht.temperature
        hum = dht.humidity

        print("Temperature:", temp, "C")
        print("Humidity:", hum, "%")

    except Exception as e:
        print("Sensor Error:", e)

    time.sleep(2)