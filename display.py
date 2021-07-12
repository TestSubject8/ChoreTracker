from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.lcd.device import pcd8544
from signal import pause
import mysql.connector as mc
import paho.mqtt.client as mq

#   Setting up the various structures to handle the devices (definitely move to a single init script and push a handler child script to the background)

def setup():
    # Nokia display setup
    contrast = 50
    serial = spi(port=0, device=1) #, gpio_DC=24, gpio_RST=25)
    display = pcd8544(serial, rotate=0)
    # bbox = display.bounding_box
    display.show()
    display.clear()
    display.contrast(contrast)

    # MQTT setup
    mqc = mq.Client()
    mqc.on_connect = show_connect
    mqc.on_message = handle_message
    mqc.connect('localhost', 1883, 60)

    # SQL DB connection
    cnx = mc.connect(user='derp', password='Lemmein', host='192.168.0.185', database='Events', charset='utf8',) # Yes I left the password here. What are you gonna do with it? Everything is local. Take that, best practices. 
    cur = cnx.cursor()
    return display, cnx, cur, mqc

# Setting up the device objects and their callbacks

def show_connect(client, userdata, flags, rc):
    print(f'Connected with {rc}')

    #client.subscribe("Rotary/left")
    client.subscribe("draw")

def handle_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    print(f'Message on {message.topic}, says {msg}')
    l = msg.split(',')
    a, b, text = tuple(l)
    draw(int(a),int(b), text)

# with canvas(display) as draw:
#     draw.text((0,0), "Testing display and rot", fill='white')
# pause()

def draw(a,b, text):
    with canvas(display) as draw:
        draw.rectangle(display.bounding_box, fill='black', outline='white')
        draw.line([15,0,15,47], fill='white', width=1)
        draw.multiline_text((a, b), text, fill='white')
            # a,b, text, fill='white', spacing=2)
    # pause()

# display.backlight(False)
if __name__ == '__main__':
    display, cnx, cur, mqc = setup()
    cur.execute("select database()")
    d = cur.fetchone()
    draw(17,3, d[0])
    mqc.loop_forever()