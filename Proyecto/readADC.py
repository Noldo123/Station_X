#!/usr/bin/python
import Adafruit_BBIO.ADC as ADC
import time
import math
import Adafruit_CharLCD as LCD

#sensor adc
sensor = "P9_40"
#lcd part
lcd_rs = 'P8_8'
lcd_en = 'P8_10'
lcd_d4 = 'P8_18'
lcd_d5 = 'P8_16'
lcd_d6 = 'P8_14'
lcd_d7 = 'P8_12'
lcd_backLight = 'P8_7'#columnas LCD
lcd_columns = 16
lcd_rows = 1

lcd = LCD.Adafruit_CharLCD(lcd_rs,lcd_en,lcd_d4,lcd_d5,lcd_d6,lcd_d7,lcd_columns,lcd_rows,lcd_backLight)

ADC.setup()

while True:
    reading = ADC.read(sensor)
    lcd.message('Iniciando')
    time.sleep(5.0)
    # voltage= reading *3.3
    temp = 115*reading
    time.sleep(1)
    print "La temperatura es: " + str(temp) + " C"
    lcd.message('Temp. : ' + str(temp))
    lcd.clear()