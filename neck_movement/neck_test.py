from __future__ import division
import time
import math
import random

import Adafruit_PCA9685

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

# Initialize servo channel for each AU

#---EYES--- (front Pi)
#8 and 9 are left right; 7 is up down; 6 and 5 are eyelids
#8 and 9: quickness 10; 310 to 390 pulse (neutral 350)
#7: quickness 10; 350 to 480 pulse (neutral 450)
#5 (right) and 6 (left): quickness 10; 375 to 550 (neutral 550)

servo1 = 8
servo2 = 7
servo3 = 6
servo4 = 5
servo5 = 9

#---NECK--- (front Pi)
servo6 = 15
servo7 = 14
servo8 = 13
servo9 = 12
servo10 = 11
servo11 = 10



#Time delay when rotating servo horn (seconds)
delay = 0.015

def neckNod():
    max_pulse = 475 # Defining max starting positions
    min_pulse = 275
    quickness = .5
    x = 0
    pos = 375
    opposite = 0
    servo9_pos = 0
    servo7_pos = 0
    servo10_pos = 0
    deg = 0
    rad = 0
    a = 0
    #600-150=450; 1 deg ~= 2.5 pulses; 0 deg ~= 150 and 180 deg ~= 600
   

    time_start = time.time()
    #time_end = 0

    diff = (max_pulse - min_pulse)/2


    while True: 

        a = math.sin(rad)
        #print(a)
        pos = int((a*diff)+375)
        #print(pos)
        if(x == 0 and pos <= max_pulse):
            deg = deg + quickness
        else:
            x = 1
            
        if(x == 1 and pos >= min_pulse):
            deg = deg - quickness
        else:
            x = 0

        rad = (deg*3.1415)/180
        #print('y')
        opposite = 750 - pos # 600 - pos + 150
        servo9_pos = pos + 75 # 30 degrees = 75 pulses
        servo7_pos = opposite 
        servo10_pos = opposite - 75
        pwm.set_pwm(servo6,0,pos)
        pwm.set_pwm(servo7,0,servo7_pos)
        pwm.set_pwm(servo9,0,servo9_pos)
        pwm.set_pwm(servo10,0,servo10_pos)
        time.sleep(0.001)

        time_end = time.time()
        if((time_end - time_start) > 1.5):
            time.sleep(0.5)
            pwm.set_pwm(servo6,0,375)
            pwm.set_pwm(servo7,0,375)
            pwm.set_pwm(servo8,0,375)
            pwm.set_pwm(servo9,0,375)
            pwm.set_pwm(servo10,0,375)
            pwm.set_pwm(servo11,0,375)
            time.sleep(0.5)
            break

neckNod()

