from machine import Pin
import utime

tick = 0

def irq_handler(pin):
    global tick
    tick += 1
    print("{}th IRQ with flags:".format(tick, pin.irq().flags()))

p2 = Pin(2, Pin.IN, Pin.PULL_UP)
p2.irq(irq_handler, Pin.IRQ_FALLING)
# p2.irq(lambda pin: print("IRQ with flags:", pin.irq().flags()), Pin.IRQ_FALLING)

while True:
    utime.sleep(2)