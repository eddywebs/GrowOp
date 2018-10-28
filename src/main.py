import RPi.GPIO as GPIO
import logging, sys
from flask import Flask
app = Flask(__name__)
app.config.from_pyfile('dev.cfg')

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

@app.route('/')
def hello_world():
    return 'Hello World! from fask'

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

if __name__ == '__main__':
    try:
        setup()
        logging.debug('initialized the gpio setup')
        app.run(host='0.0.0.0', port=80)
        logging.info('ok initialized all the stuff here it goes')
    except KeyboardInterrupt: # catch *all* exceptions
        destroy()
        pass #do whatever elese you wanna do
        logging.debug('dont act a foo ! just checking if this will print?')










