from adafruit_servokit import ServoKit
import time
open_angle = 80
close_angle = 120
kit = ServoKit(channels=16)

left_eye_ball_x = 67  #-90 left | 67 max_left | 112 max_right |  
left_eye_ball_y = 90  #-90 up | 70 max_up | 130 max_down |

right_eye_ball_x = 70 #-90 left | 112 max_right | max_left 70 |
right_eye_ball_y = 90 #-90 down
kit.servo[2].actuation_range = 180
kit.servo[3].actuation_range = 180
kit.servo[4].actuation_range = 180
kit.servo[5].actuation_range = 180
#kit.servo[1].actuation_range = 180
#kit.servo[1].angle = close_angle
#kit.servo[0].actuation_range = 180
#kit.servo[0].angle = close_angle

time.sleep(.3)

#kit.servo[1].actuation_range = 180
#kit.servo[1].angle = open_angle
#kit.servo[0].actuation_range = 180
#kit.servo[0].angle = open_angle

def eye_blink():

    kit = ServoKit(channels=16)
    
    kit.servo[1].actuation_range = 180 
    kit.servo[0].actuation_range = 180
    kit.servo[1].angle = 140
    kit.servo[0].angle = 120

    time.sleep(.3)

    kit.servo[1].angle = 80
    kit.servo[0].angle = 90


def left_side_eye_ball_movement(x_angle,y_angle):
      
    kit = ServoKit(channels=16)
    kit.servo[2].actuation_range = 180
    kit.servo[3].actuation_range = 180
    kit.servo[2].angle = x_angle 
    kit.servo[3].angle = y_angle

def right_side_eye_ball_movement(x_angle,y_angle):
    
    kit = ServoKit(channels=16)
    kit.servo[4].actuation_range = 180
    kit.servo[5].actuation_range = 180
    kit.servo[4].angle = x_angle
    kit.servo[3].angle = y_angle


while True:

    left_side_eye_ball_movement(90,90)
    right_side_eye_ball_movement(90,90)

    time.sleep(1)
    eye_blink()

    left_side_eye_ball_movement(90,90)
    right_side_eye_ball_movement(90,90)
    
    time.sleep(1)

    eye_blink()

    




    



    
    



