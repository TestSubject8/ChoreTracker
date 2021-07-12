import paho.mqtt.client as mq
from signal import pause
import RPi.GPIO as GPIO
import Encoder

# General gpio setup for the raspi0
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT) # backlight pin

for x in [26, 17]:  # push buttons (encoders)
    GPIO.setup(x, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

def show_connect(client, userdata, flags, rc):
    print(f'Connected with {rc}')

    client.subscribe("Rotary/left")
    client.subscribe("Rotary/right")

def handle_message(client, userdata, msg):
    print(f'{msg.topic} says {msg.payload}')

def updater(channel):
    display.contrast(contrast+channel) 

def query_again(channel):
    cur.execute("select database()")
    d = cur.fetchone()
    draw(17,3, d[0])


client = mq.Client()
client.on_connect = show_connect
client.on_message = handle_message

client.connect('localhost', 1883, 60)

enc_0 = Encoder.Encoder(27,22, updater)

GPIO.add_event_detect(17, GPIO.RISING, callback=query_again, bouncetime=400)

pause()

