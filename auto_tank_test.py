# -*- coding: utf-8 -*-
import ASUS.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

Forward = 0
Backward = 1
Stop = 2

HIGH = 1
LOW = 0

def setPinConfig(en, ina, inb):
    GPIO.setup(en, GPIO.OUT)
    GPIO.setup(ina, GPIO.OUT)
    GPIO.setup(inb, GPIO.OUT)
    pwm = GPIO.PWM(en, 100)
    pwm.start(0)
    return pwm
class Motor():
    def __init__(self,En, Ina, Inb):
        self.speed = 0
        self.stat = 0
        self.Ina = Ina
        self.Inb = Inb
        self.pwm = setPinConfig(En, Ina, Inb)
    def setMotor(self, speed, elec_stat):
        self.pwm.ChangeDutyCycle(speed)
        if elec_stat == Forward:
            GPIO.output(self.Ina, LOW)
            GPIO.output(self.Inb, HIGH)
        elif elec_stat == Backward:
            GPIO.output(self.Ina, HIGH)
            GPIO.output(self.Inb, LOW)
        elif elec_stat == Stop:
            GPIO.output(self.Ina, LOW)
            GPIO.output(self.Inb, LOW)

Left_track = Motor(32, 38, 36)
Right_track = Motor(33, 37, 35)
turret_rotation = Motor(24, 16, 22)
gun_tilt = Motor(19, 21, 23)
gun_reload = Motor(27, 29, 31)

try:
    while True:
        Left_track.setMotor(50, Forward)
        Right_track.setMotor(50, Backward)
except KeyboardInterrupt:
    print("\n ctrl c 입력")

GPIO.cleanup()