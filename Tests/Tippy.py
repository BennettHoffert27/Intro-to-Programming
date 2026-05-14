import time
from adafruit_circuitplayground import cp
while True:
    cp.pixels.brightness = 0.0618
    x,y,z = cp.acceleration
    if cp.acceleration:
        threshold = 10
        if abs(x) > threshold:
            for i in range (0,3):
               cp.pixels[i] = (0,255,0)
        else:
            for i in range (5,8):
                cp.pixels[i] = (255, 0,0)
    if abs(z) > threshold:
        for i in range(0,3):
            cp.pixels[i] = (0,0,0)
