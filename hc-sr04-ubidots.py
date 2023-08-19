import RPi.GPIO as GPIO
import time
from ubidots import ApiClient

# Create an ApiClient object
api = ApiClient(token='BBFF-4FL4xCOfJBXeE2WHs5IxKGhOElfWsD')

while True:
    try:
        variable1 = api.get_variable("64dc8dfb421b231ef9199c46")
        
        GPIO.setmode(GPIO.BOARD)

        PIN_TRIGGER = 7
        PIN_ECHO = 11

        GPIO.setup(PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(PIN_ECHO, GPIO.IN)

        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        #print ("Waiting for sensor to settle")

        #time.sleep(2)

        #print ("Calculating distance")

        GPIO.output(PIN_TRIGGER, GPIO.HIGH)

        time.sleep(0.00001)

        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        while GPIO.input(PIN_ECHO)==0:
            pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO)==1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)
        print ("Distance:",distance,"cm")
      
        variable1.save_value({'value': distance})
        print ("Value sent")
    except ValueError:
        print ("Value not sent") 
