import time
import board
import busio
import keypad
import displayio
import terminalio
import usb_hid

import adafruit_displayio_ssd1306

from adafruit_display_text import label
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode




displayio.release_displays()

i2c = busio.I2C(board.D5, board.D4)

display_bus = displayio.I2CDisplay(
    i2c,
    device_address=0x3C
)

display = adafruit_displayio_ssd1306.SSD1306(
    display_bus,
    width=128,
    height=32,
)

splash = displayio.Group()

title = label.Label(
    terminalio.FONT,
    text="Spotify PlayDeck",
    color=0xFFFFFF,
    x=5,
    y=10,
)

status = label.Label(
    terminalio.FONT,
    text="Booting...",
    color=0xFFFFFF,
    x=20,
    y=25,
)

splash.append(title)
splash.append(status)

display.root_group = splash=


time.sleep(2)

status.text = "Ready"



cc = ConsumerControl(usb_hid.devices)


keys = keypad.Keys(
    (
        board.D0,
        board.D1,
        board.D2,
        board.D3,
    ),
    value_when_pressed=False,
    pull=True,
)

print("Spotify PlayDeck Ready")



last_action = time.monotonic()


def show(text):
    global last_action
    status.text = text
    last_action = time.monotonic()


while True:

    event = keys.events.get()

    if event and event.pressed:

        if event.key_number == 0:
            cc.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
            show("Previous Track")

        elif event.key_number == 1:
            cc.send(ConsumerControlCode.PLAY_PAUSE)
            show("Play / Pause")

        elif event.key_number == 2:
            cc.send(ConsumerControlCode.VOLUME_INCREMENT)
            show("Volume +")

        elif event.key_number == 3:
            cc.send(ConsumerControlCode.VOLUME_DECREMENT)
            show("Volume -")

    if time.monotonic() - last_action > 3:
        if status.text != "Ready":
            status.text = "Ready"

    time.sleep(0.01)