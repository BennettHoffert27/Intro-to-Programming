from adafruit_circuitplayground import cp
import time
while True:
   cp.pixels.brightness = 0.0618
   cp.pixels.fill((0,200,200))
   time.sleep(0.367)
   cp.pixels.fill((0,0,0))
   time.sleep(0.367)