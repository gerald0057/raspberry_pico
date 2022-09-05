from machine import Pin
import utime

PIN_HIGH = 1
PIN_LOW = 0

pin_led = Pin(25, Pin.OUT)

while True:
    pin_led.value(PIN_HIGH)
    utime.sleep(0.1)
    pin_led.value(PIN_LOW)
    utime.sleep(0.1)