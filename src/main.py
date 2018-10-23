import RPi.GPIO as GPIO
from flask import Flask
app = Flask(__name__)

Relay_channel = [17, 18]

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(Relay_channel, GPIO.OUT, initial=GPIO.LOW)
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
	i=0
	GPIO.output(Relay_channel[i], GPIO.HIGH)
	return '...Relay channel %d on' % (i+1)
	
@app.route('/off')
def turn_off1():
	i=0
	GPIO.output(Relay_channel[i], GPIO.LOW)
	return '...Relay channel %d on' % (i+1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
