from adafruit_circuitplayground import cp
import time
while True:
    cp.pixels.brightness = 0.0618
    for i in range(0,2):
        while i == 1:
            cp.pixels.fill((0,0,175))
            time.sleep(0.25)
            i += 1
        while i == 2:
            cp.pixels.fill((175,0,0))
            cp.play_tone(500,0.25)
            time.sleep(0.25)
            i -= 1