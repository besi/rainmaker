import os
import time
from machine import Pin


from machine import SoftSPI, Pin, SDCard
import os

sd = SDCard(sck=1, miso=0, mosi=2, cs=3)
os.mount(sd, "/sd")  # mount


from wavplayer import WavPlayer

BUFFER_LENGTH_IN_BYTES = 2000
I2S_ID = 0

wp = WavPlayer(
    id=I2S_ID,
    sck_pin=Pin(10),
    ws_pin=Pin(6),
    sd_pin=Pin(8),
    ibuf=2000,
)

wp.play("rain.wav", loop=True)
while wp.isplaying() == True:
    pass

