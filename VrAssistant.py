from __future__ import division
import pyaudio
import wave
import pvporcupine
import struct
import speech_recognition as sr
import os
from gtts import gTTS
import openai
from pvrecorder import PvRecorder
import time
#import Adafruit_PCA9685
#from adafruit_servokit import ServoKit
from mutagen.mp3 import MP3
import threading


#pwm =Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
#servo_min = 150  # Min pulse length out of 4096
#servo_max = 600  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.

"""pen_angle = 80
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
"""

def audio_length():
    audio = MP3("audio.mp3")
    return audio.info.length
"""
def eye_blink(): 
    
    open_angle = 80
    close_angle = 120
    kit = ServoKit(channels=16)
    kit.servo[1].actuation_range = 180
    kit.servo[1].angle = 140
    kit.servo[0].actuation_range = 180
    kit.servo[0].angle = 120

    time.sleep(.3)

    kit.servo[1].actuation_range = 180
    kit.servo[1].angle = 80
    kit.servo[0].actuation_range = 180
    kit.servo[0].angle = 90

    time.sleep(2)
    
"""
"""
def look_left_right():
    while(True):

        left_side_eye_ball_movement(67,90)
        right_side_eye_ball_movement(70,90)

        time.sleep(1.5)
        eye_blink()

        left_side_eye_ball_movement(112,90)
        right_side_eye_ball_movement(112,90)
        
        time.sleep(1.5)

        eye_blink()
       # count = count + 1
        
def eye_ball():
    count = 0

    while(count > 4):

        left_side_eye_ball_movement(67,90)
        right_side_eye_ball_movement(70,90)

        time.sleep(1)

        left_side_eye_ball_movement(112,90)
        right_side_eye_ball_movement(112,90)
        
        time.sleep(1)

        count = count + 1
    


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

def angry_face_eyelid():
    open_angle = 120
    close_angle = 120
    kit = ServoKit(channels=16)
    kit.servo[0].actuation_range = 180
    kit.servo[0].angle = close_angle
    kit.servo[1].actuation_range = 180
    kit.servo[1].angle = close_angle       

def jaw_movement():
    
    j = 90
    i = 90
     
    close_angle_i = 110
    close_angle_j = 70
    # Set channels to the number of servo channels on your kit.
    # 8 for FeatherWing, 16 for Shield/HAT/Bonnet.

    kit = ServoKit(channels=16)
    kit.servo[6].actuation_range = 180
    kit.servo[6].angle = i
    kit.servo[7].actuation_range = 180
    kit.servo[7].angle = i

    time.sleep(1)

    kit.servo[6].actuation_range = 180
    kit.servo[6].angle = close_angle_i
    kit.servo[7].actuation_range = 180
    kit.servo[7].angle = close_angle_j

    time.sleep(2)

    
    #kit.servo[6].actuation_range = 180
    #kit.servo[6].angle = i
    #kit.servo[7].actuation_range = 180
    #kit.servo[7].angle = i
    
"""


""" def speak_movement(audio_length):

    now = time.time()
    timer = 0

    while(timer != audio_length):
        end = time.time()
        j = 90
        i = 90
         
        close_angle_i = 110
        close_angle_j = 70
        # Set channels to the number of servo channels on your kit.
        # 8 for FeatherWing, 16 for Shield/HAT/Bonnet.

        kit = ServoKit(channels=16)
        kit.servo[6].actuation_range = 180
        kit.servo[6].angle = i
        kit.servo[7].actuation_range = 180
        kit.servo[7].angle = i

        time.sleep(.3)

        kit.servo[6].actuation_range = 180
        kit.servo[6].angle = close_angle_i
        kit.servo[7].actuation_range = 180
        kit.servo[7].angle = close_angle_j

        time.sleep(1)

        
        #kit.servo[6].actuation_range = 180
        #kit.servo[6].angle = i
        #kit.servo[7].actuation_range = 180
        #kit.servo[7].angle = i
        timer = round(end-now)
 

def surprise_face_eyelid():
    open_angle = 70
    close_angle = 70
    kit = ServoKit(channels=16)
    kit.servo[0].actuation_range = 180
    kit.servo[0].angle = close_angle
    kit.servo[1].actuation_range = 180
    kit.servo[1].angle = close_angle       

def set_servo_pulse(channel, pulse):
    # Set frequency to 60hz, good for servos.

    pwm.set_pwm_freq(60)
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)


def servo_movement():

    while True:
        pwm.set_pwm(0, 0, servo_min)
        time.sleep(1)
        pwm.set_pwm(0, 0, servo_max)
        time.sleep(1)
"""

def openai_gpt3(recognized_text):
    #print(recognized_text);

    openai.api_key = "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"

    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "
    text_input = recognized_text
    print("Debug test" + text_input);

    while True:

        response = openai.Completion.create(
          engine="text-davinci-002",
          prompt="The following is a conversation with an AI humanoid robot lab assistant named rocky. The robot is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: My name is rocky\nHuman: who created you?\nAI:Iam was created by team tech Mutants\nHuman:How can you help me\nAI: I can can guide through various experiments in the laboratory and i can provide instructions to do experiments\nHuman:"+ text_input,
          temperature=0.9,
          max_tokens=150,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0.6,
          stop=[" Human:", " AI:"]
        )
        print(response)
        text = response['choices'][0]['text']
        text = text[4:]
        text = text.split(' ', 1)[1]

        return text


def speak(text):
    
    language = 'en-IN'
    myobj = gTTS(text=text, lang=language, slow=True)
    myobj.save("audio.mp3")
    audio = audio_length()
    #t4 = threading.Thread(target=speak_movement,args=(audio))
    os.system("mpg321 audio.mp3" +" tempo 10.9")
    
    print("audio length is :")
    print(audio)


def speech_recognizer():

    r = sr.Recognizer()

    while True:

        with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Say Something")
                audio = r.listen(source)

                try:
                        text = r.recognize_google(audio)
                        print("you said: " + text)
                        break


                except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio")

                except sr.RequestError as e:
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return text

def wake_word_detection():

    porcupine = pvporcupine.create(
                access_key = "6rUtqqqPW84yy+2ouTmCs5Wmfkmv1QIxDjUXzN8WUDR1b9MxUKhi3w==",
                keyword_paths=['hey_rocky.ppn']
                        )

    #porcupine = pvporcupine.create(
    #                access_key='6rUtqqqPW84yy+2ouTmCs5Wmfkmv1QIxDjUXzN8WUDR1b9MxUKhi3w==',
    #                keywords=['picovoice', 'bumblebee']
    #                )

    #devices = PvRecorder.get_audio_devices()

    #recorder = PvRecorder(device_index= 1, frame_length=porcupine.frame_length)
    #recorder.start()

     
    CHUNK = porcupine.frame_length
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = porcupine.sample_rate
    p = pyaudio.PyAudio()

    stream = p.open(format =FORMAT,
                    channels =CHANNELS,
                    input_device_index=None,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    
    print("start recording..")

    frames = []

    while True:
        data = stream.read(CHUNK,exception_on_overflow = False)
        #pcm = recorder.read()
        #audio_frame =  porcupine.process(pcm)
        audio_frame = struct.unpack_from('h' * CHUNK,data)
        keyword_index = porcupine.process(audio_frame)
        #eye_blink()
        if keyword_index == 0:
            print("hey rocky") 
            speak("yes") 
            stream.stop_stream()
            stream.close()
            p.terminate()
            #eye_blink()
            #jaw_movement()
            input_text = speech_recognizer()
            print(input_text)
            if 'angry' in input_text:
                #servo_movement()
                angry_face_eyelid()
                break
            elif 'surprise' in input_text:
                surprise_face_eyelid()
                break
            elif 'violence' in input_text:
                speak("violence vioolence violence i don't like it i avoid, but violence likes me i can't avoid")

            elif input_text:
                response = openai_gpt3(input_text)
                speak(response)
                break


    print("recording stopped")
    
def main():
    while True:
        #eye_blink()
        wake_word_detection()
        #eye_blink()
        #look_left_right()

    #print(speech_recognizer())

if __name__ == '__main__':
    #t1 = threading.Thread(target=look_left_right)
    #t2 = threading.Thread(target=wake_word_detection)
    #t3 = threading.Thread(target=jaw_movement)
    #t5 = threading.Thread(target=eye_ball)

    #t1.start()
    #t2.start()
    #t3.start()
    #t5.start()

    main()

