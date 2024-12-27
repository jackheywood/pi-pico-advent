from machine import Pin
import time

# Set up buttons with GPIO pin numbers
# Set pin as input and use a pull down
button1 = Pin(3, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(13, Pin.IN, Pin.PULL_DOWN)

# Set up LEDs with GPIO pin numbers
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

while True: # Loop forever
    
    time.sleep(0.2) # Short delay

    if button1.value() == 1:
        red.toggle()
        
    if button2.value() == 1:
        amber.toggle()
        
    if button3.value() == 1:
        green.toggle()