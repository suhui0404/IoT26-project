from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2)

label = "plastic"  # AI 분류 결과

lcd.clear()

lcd.write_string(label.upper())

lcd.cursor_pos = (1, 0)

if label == "plastic":
    lcd.write_string("PUT INSIDE")
elif label == "paper":
    lcd.write_string("PUT INSIDE")
elif label == "metal":
    lcd.write_string("PUT INSIDE")
elif label == "glass":
    lcd.write_string("PUT INSIDE")
else:
    lcd.write_string("PUT INSIDE")