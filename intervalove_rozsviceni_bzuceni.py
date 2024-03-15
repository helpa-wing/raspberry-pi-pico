from machine import Pin, Timer, PWM
from utime import sleep_ms

buzzer = PWM(Pin(15)) # kde budeme PWM generovat
#buzzer.freq(500) # frekvence 500 Hz

button = Pin(5, Pin.IN, Pin.PULL_UP)
inbuiltLed = 10
led = Pin(inbuiltLed, Pin.OUT)

def blik(svitivost,cas): # funkce blik rozsvěcí led svitivostí ¨svitivost¨*10% a na dobu "cas" milisekund
    setina_casu= cas/100
    for i in range(10): # čas rozdělíme na 10 úseků
        led.value(1) # rozsviť
        sleep_ms(round(setina_casu*svitivost)) # počkej svítivost desetin úseku 
        led.value(0) # zhasni
        sleep_ms(round(setina_casu*(10-svitivost))) # počkej zbytek do úseku

while True:
    while button.value() == 1:
        sleep_ms(1)
    print ("Zahrajeme melodii")
    buzzer.duty_u16(32768) # strida PWM 0...65535, 50%
    for i in range (11): # nastav pocitadlo od 0 do 10
        buzzer.freq(500+i*250)
        blik(i, 227) # rozsvit v úrovni 0 az 10 na dobu 227ms
    for i in range (11):
        buzzer.freq(500+(10-i)*250)        
        blik(10-i, 227) # rozsvit v úrovni 10 do 0 na dobu 227ms
    buzzer.duty_u16(0) # hlasitost PWM 0...65535, 50%
    print ("Tradá stop")