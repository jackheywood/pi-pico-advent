from machine import Pin
import time

# Set up LED names and GPIO pin numbers
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

counter = 1
sleepTime = 0.33333

while counter <= 10:
    print(counter)
    
    # Red on
    red.value(1)
    amber.value(0)
    green.value(0)

    time.sleep(sleepTime)

    # Amber on
    red.value(0)
    amber.value(1)
    green.value(0)
    
    time.sleep(sleepTime)

    # Green on
    red.value(0)
    amber.value(0)
    green.value(1)
    
    time.sleep(sleepTime)
    
    counter +=1

# All off
red.value(0)
amber.value(0)
green.value(0)