from machine import Pin, PWM
from utime import sleep_ms

__version__ = '1.0.0'
__author__ = 'Ahnaf Tahmid'
__licence__ = 'MIT License'

class GMtube:
    '''
    To run Geiger tube at desaired voltage. Example- for SBM-20 the required voltage is 400v.
    PWM is used to generate the high voltage and a event pin is used to collect discharged event
    '''
    # at the start count is 0
    count = 0
    def __init__(self,pwm=12,freq=20000,duty=675,event=15):
        self.freq=freq
        self.duty=duty
        
        #HV pin 12, freq 20kHz, duty 66%
        self.pwmpin = PWM(Pin(pwm), freq=freq, duty=duty)
        #event pin 15
        self.discharge = Pin(event, Pin.IN)
        self.discharge.irq(trigger=Pin.IRQ_FALLING, handler= self.handle)

    # Function to be called when the interrupt triggers
    def handle(self,p):
        global count
        self.count+=1

class Buzzer:
    '''
    A buzzer can be used to detect radiation. To make Geiger counter noise two pin can be used for input and output.
    Here when one pin is in on condition other will be off.
    '''
    def __init__(self,pin1=2,pin2=4):
        self.pin_1 = Pin(pin1, Pin.OUT)
        self.pin_2 = Pin(pin2, Pin.OUT)
        self.buzzer()
    def buzzer(self):
        self.pin_1.on()
        self.pin_2.off()
        # this goes into dead time of the counter
        sleep_ms(2)
        self.pin_1.off()
        self.pin_2.on()
        sleep_ms(2) 
        self.pin_2.off()
