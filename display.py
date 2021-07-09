from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.lcd.device import pcd8544
from signal import pause
import RPi.GPIO as GPIO
import Encoder
import mysql.connector as mc

#   Setting up the various structures to handle the devices (definitely move to a single init script and push a handler child script to the background)

# General gpio setup for the raspi0
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT) # backlight pin

for x in [26, 17]:  # push buttons (encoders)
    GPIO.setup(x, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

# Nokia display setup
contrast = 50
serial = spi(port=0, device=1) #, gpio_DC=24, gpio_RST=25)
display = pcd8544(serial, rotate=0)
# bbox = display.bounding_box
display.show()
display.clear()
display.contrast(contrast)

# SQL DB connection
cnx = mc.connect(user='derp', password='Lemmein', host='192.168.0.185', database='Events', charset='utf8',) # Yes I left the password here. What are you gonna do with it? Everything is local. Take that, best practices. 
cur = cnx.cursor()

# Setting up the device objects and their callbacks

def updater(channel):
    display.contrast(contrast+channel)

def query_again(channel):
    cur.execute("select database()")
    d = cur.fetchone()
    draw(17,3, d[0])

enc_0 = Encoder.Encoder(27,22, updater)

GPIO.add_event_detect(17, GPIO.RISING, callback=query_again, bouncetime=400)

# with canvas(display) as draw:
#     draw.text((0,0), "Testing display and rot", fill='white')
# pause()

def draw(a,b, text):
    with canvas(display) as draw:
        draw.rectangle(display.bounding_box, fill='black', outline='white')
        draw.line([15,0,15,47], fill='white', width=1)
        draw.multiline_text([a,b], text, fill='white', spacing=2)
    # pause()

# display.backlight(False)
if __name__ == '__main__':
    cur.execute("select database()")
    d = cur.fetchone()
    draw(17,3, d[0])
    pause()
