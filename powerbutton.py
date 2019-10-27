import time
import RPi.GPIO as GPIO
import os

pwr_bt=3
ledx =4 

def buttonEvent(channel1):
    # sysytem shutdown with "Wake From Halt Function"
    os.system("sudo shutdown -h now")

GPIO.setmode(GPIO.BCM)

# The led includ in SW
GPIO.setup(ledx,GPIO.OUT)
GPIO.output(ledx,GPIO.HIGH)

#GPIO3(No.5) is input.
GPIO.setup(pwr_bt,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(pwr_bt, GPIO.FALLING, callback=buttonEvent, bouncetime=300) 

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    exit()
