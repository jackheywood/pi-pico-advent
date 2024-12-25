from machine import Pin
import time

# Set up LED names and GPIO pin numbers
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

counter = 1
sleepTime = 0.1

while counter < 100:
    print(counter)
    
    # LEDs all on
    red.value(1)
    amber.value(1)
    green.value(1)

    time.sleep(sleepTime)

    # LEDs all off
    red.value(0)
    amber.value(0)
    green.value(0)
    
    time.sleep(sleepTime)
    
    counter +=1