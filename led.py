import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)#Bread
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
print "LED on"
GPIO.output(17,GPIO.HIGH)
time.sleep(5)
print "LED no"
GPIO.output(17,GPIO.LOW)
