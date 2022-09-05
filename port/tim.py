from machine import Pin, Timer

pin_led = Pin(25, Pin.OUT)
tim = Timer()

def tick(timer):
    global pin_led
    pin_led.toggle()

tim.init(freq=10, mode=Timer.PERIODIC, callback=tick)