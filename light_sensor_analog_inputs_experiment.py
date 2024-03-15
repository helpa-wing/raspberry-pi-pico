'''
Goal: Make the Pico’s on-board LED turn on when it gets dark and off when it’s bright.
How it works: • The Pico has a controllable LED connected to GP25.
              • There’s a light sensor (phototransistor) linked to Analogue-In A0, powered at 3.3V.
              • The sensor reads light levels; bright light means a high value, dark means a low value.
              • When it gets dark, the on-board LED automatically turns on.
'''
import machine
from time import sleep

lightSensor = machine.ADC(27) # Set up the anakogue (AD) on GP26 with a human−readable name
LED =  machine.Pin(25, machine.Pin.OUT) # Set up the onboard LED Pin as an output

lightLevelToSwitchAt = 13000 # Set to about 20% of scale − Pico ADC is 0 to 65535

# THe loop function runs forever, reading the light levell and turning on the LED if it's dark
while True:
    # First read the led value oon the analog input
    lightValue = lightSensor.read_u16()
    print (lightValue)
     #now decide what to do
    if (lightValue > lightLevelToSwitchAt): # Then it id bright, so turn off the LED
        LED.value(0) # Turn the LED off
    else:
        LED.value(1) # Turn the LED on
    sleep (1)
