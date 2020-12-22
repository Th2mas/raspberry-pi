#!/usr/bin/env python3
from gpiozero import LED
from time import sleep

led = LED(24)
speedInSeconds = 1

for i in range(3):
    led.toggle()
    sleep(speedInSeconds)
    led.toggle()
    sleep(speedInSeconds)
