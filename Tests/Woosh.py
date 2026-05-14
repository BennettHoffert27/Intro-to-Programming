import time
from adafruit_circuitplayground import cp
while True:
    for i in range(10):
        a = 0
        if cp.button_a:
            cp.pixels[a] = (0,255,0)