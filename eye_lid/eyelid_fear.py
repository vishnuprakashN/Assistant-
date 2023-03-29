from __future__ import division
import time
import math
import random

import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685(0x41)

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

# Initialize servo channel for each AU

#---EYES--- (front Pi)

#5 (right) and 6 (left): quickness 10; 375 to 550 (neutral 550)

servo3 = 6
servo4 = 5

#Time delay when rotating servo horn (seconds)
delay = 0.015

total_time_start = time.time()

def eyelids():
    pwm.set_pwm(servo3,0,210) #eyelids resting point 235
    pwm.set_pwm(servo4,0,575)

    time.sleep(3)

    pwm.set_pwm(servo3,0,235) #eyelids resting point 235
    pwm.set_pwm(servo4,0,550) #550 ...lower range should be 375 for servo4 and 520 for servo3pwm.set_    
        
eyelids()

