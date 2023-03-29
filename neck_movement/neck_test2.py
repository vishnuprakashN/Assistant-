from __future__ import division
import time
import math
import random

pwm = Adafruit_PCA9685.PCA9685()


# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096 (150)
servo_max = 600  # Max pulse length out of 4096 (600)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)


servo1 = 15
servo2 = 14
servo3 = 13
servo4 = 12

delay = 0.015

def neckNod():
    

















