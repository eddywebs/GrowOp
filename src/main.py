import logging, sys
from time import sleep
import importlib.util


#log config starts here 
logging.basicConfig(filename="growop.log", level=logging.DEBUG)
logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')


#log config code ends here

try:
    importlib.util.find_spec('RPi.GPIO')
    logging.debug('found the original Rpi.GPIO')
except ImportError:
    import os
    os.environ['GPIOZERO_PIN_FACTORY'] = os.environ.get('GPIOZERO_PIN_FACTORY', 'mock')
    logging.debug('fake it till you make bruh')
    
import gpiozero
from gpiozero import Device, Button, LED

from flask import Flask
app = Flask(__name__)
app.config.from_pyfile('dev.cfg')
relay17 = LED(17)

@app.route('/')
def hello_world():
    return 'Hello World! from fask'

@app.route('/on17')
def turn_on17():
    relay17.on()
    logging.info('turned on relay 17')
    logging.debug(relay17.value)
    return 'turned on relay 17'

@app.route('/check17')
def check_r17():
    foo = relay17.value
    return str(foo)


############################################

Relay_channel = [17, 18]

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Relay_channel, GPIO.OUT, initial=GPIO.HIGH)
    print ("|=====================================================|")
    print ("|         2-Channel High trigger Relay Sample         |")
    print ("|-----------------------------------------------------|")
    print ("|                                                     |")
    print ("|          Turn 2 channels on off in orders           |")
    print ("|                                                     |")
    print ("|                    17 ===> IN2                      |")
    print ("|                    18 ===> IN1                      |")
    print ("|                                                     |")
    print ("|=====================================================|")

def destroy():
    GPIO.output(Relay_channel, GPIO.LOW)
    GPIO.cleanup()


@app.route('/on')
def turn_on1():
    setup()
    i=1
    GPIO.output(Relay_channel[i], GPIO.LOW)
    return '...Relay channel %d on' % (i+1)
    
@app.route('/off')
def turn_off1():
    setup()
    i=1
    GPIO.output(Relay_channel[i], GPIO.HIGH)
    return '...Relay channel %d off' % (i+1)

@app.route('/cleanup')
def cleanup():
    setup()
    logging.info('cleaning up')
    destroy()
    return 'cleaing up'
######################################


if __name__ == '__main__':
    try:
        #setup()
        logging.debug('initialized the gpio setup')
        app.run(host='0.0.0.0', port=8080)
        logging.info('ok initialized all the stuff here it goes')
    except KeyboardInterrupt: # catch *all* exceptions
        destroy()
        pass #do whatever elese you wanna do
        logging.debug('dont act a foo ! just checking if this will print?')










