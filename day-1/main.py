from machine import Pin
import time

led = Pin(25, Pin.OUT)

while True:
    try:
        led.toggle()
        time.sleep(1)
    except KeyboardInterrupt:
        break
    
led.off()