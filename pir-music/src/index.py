#!/usr/bin/env python3
from gpiozero import MotionSensor
from vlc import MediaPlayer

from signal import pause
from sys import exit

pir = MotionSensor(24)
song_path = "../media/song.ogg"
p = MediaPlayer(song_path)


def toggle_playing():
    global p
    if p.is_playing():
        p.pause()
    else:
        p.play()

    # We need the next part to start the song again, as soon as the song finishes
    if p.get_time() == 0:
        p.stop()
        p = MediaPlayer(song_path)
        p.play()


pir.when_motion = toggle_playing

try:
    pause()
except KeyboardInterrupt:
    exit()
