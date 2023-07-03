# -*- coding: utf-8 -*-
import ASUS.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

Forward = 0
Backward = 1
<<<<<<< HEAD
Left = 2 
Right = 3
Stop = 4
#모터 채널
CH1 = 0
CH2 = 1
=======
Stop = 2
>>>>>>> add_class

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

Left_track = Motor(32, 38, 26)
Right_track = Motor(33, 37, 35)
turret_rotation = Motor(24, 16, 22)
gun_tilt = Motor(19, 21, 23)
gun_reload = Motor(27, 29, 31)

Left_track.setMotor(50, Forward)
Right_track.setMotor(50, Forward)

<<<<<<< HEAD
        if stat == Forward:
                GPIO.output(INA, LOW)
                GPIO.output(INB, HIGH)
        elif stat == Backward:
                GPIO.output(INA, HIGH)
                GPIO.output(INB, LOW)
        elif stat == Stop:
                GPIO.output(INA, LOW)
                GPIO.output(INB, LOW)
def setMotor(ch, speed, stat):
        if ch == CH1:
                setMotorControl(pwmA, IN1, IN2, speed, stat)
        else: setMotorControl(pwmB, IN3, IN4, speed, stat)

pwmA = setPinConfig(ENA, IN1, IN2)
pwmB = setPinConfig(ENB, IN3, IN4)

def keymap(screen):
        screen.clear()
        screen.refresh()
        try:
                while True:
                        key = screen.getch()
                        if key == curses.KEY_UP:
                                setMotor(CH1, 100, Forward)
                                setMotor(CH2, 100, Forward)
                        elif key == curses.KEY_DOWN:
                                setMotor(CH1, 100, Backward)
                                setMotor(CH2, 100, Backward)
                        elif key == curses.KEY_LEFT:
                                setMotor(CH1, 50, Forward)
                                setMotor(CH2, 50, Backward)
                        elif key == curses.KEY_RIGHT:
                                setMotor(CH1, 50, Backward)
                                setMotor(CH2, 50, Forward)
                        else:
                                setMotor(CH1, 0, Stop)
                                setMotor(CH2, 0, Stop)
                        screen.refresh()
        except KeyboardInterrupt:
                print("\nCtrl c 중지")

curses.wrapper(keymap)

GPIO.cleanup() 
=======
GPIO.cleanup()
>>>>>>> add_class
