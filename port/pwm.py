# Example using PWM to fade an LED.

import time
from machine import Pin, PWM


# Construct PWM object, with LED on Pin(25).
pwm = PWM(Pin(25))

# Set the PWM frequency.
pwm.freq(1000)

# Fade the LED in and out a few times.
duty_max = 65535
duty = duty_max
step = 100
direction = -1

while True:
    duty += step * direction
    if duty > duty_max:
        duty = duty_max
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    pwm.duty_u16(duty)
    time.sleep(0.001)