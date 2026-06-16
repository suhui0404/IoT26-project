import time
import board
import adafruit_dht

from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2)

dht = adafruit_dht.DHT11(board.D4)

while True:
    try:
        temp = dht.temperature
        hum = dht.humidity

        lcd.clear()

        lcd.write_string(f"T:{temp}C")

        lcd.cursor_pos = (1, 0)
        lcd.write_string(f"H:{hum}%")

        print(temp, hum)

    except:
        pass

    time.sleep(2)