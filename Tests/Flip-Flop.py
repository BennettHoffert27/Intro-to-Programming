import time
from adafruit_circuitplayground import cp
while True:
   cp.pixels.brightness = 0.0618
   if cp.switch:
      for i in range(0,5):
         cp.pixels[i] = ((0,255,0))
      for i in range(6,10):
         cp.pixels[i] = ((0,0,0))
   else:
      for i in range (6,10):
         cp.pixels[i] = ((0,255,0))
      for i in range (0,5):
         cp.pixels[i] = ((0,0,0))