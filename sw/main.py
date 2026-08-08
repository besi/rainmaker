import os
import time
from machine import Pin


from machine import SoftSPI, Pin, SDCard
import os

sd = SDCard(sck=0, miso=1, mosi=4, cs=5)

os.mount(sd, "/sd")

from wavplayer import WavPlayer


I2S_ID = 0
BUFFER_LENGTH_IN_BYTES = 2000


wp = WavPlayer(
    id=I2S_ID,
    sck_pin=Pin(10),
    ws_pin=Pin(6),
    sd_pin=Pin(8),
    ibuf=BUFFER_LENGTH_IN_BYTES,
)
mute = Pin(2, Pin.OUT)
mute.off()

wp.play("rain.wav", loop=True)
while wp.isplaying() == True:
    pass

