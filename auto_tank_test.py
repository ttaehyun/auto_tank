# -*- coding: utf-8 -*-
import ASUS.GPIO as GPIO
import curses

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# 전후 좌우 모터상태
Forward = 0
Backward = 1
Left = 2 
Right = 3
Stop = 4
#모터 채널
CH1 = 0
CH2 = 1

#PIN 입출력 설정
OUTPUT = 1
INPUT = 0
#PIN 설정
HIGH = 1
LOW = 0

#PWM PIN
ENA = 32
ENB = 33
#GPIO PIN
IN1 = 38
IN2 = 36
IN3 = 37
IN4 = 35

def setPinConfig(EN, INA, INB):
        GPIO.setup(EN, GPIO.OUT)
        GPIO.setup(INA, GPIO.OUT)
        GPIO.setup(INB, GPIO.OUT)
        pwm = GPIO.PWM(EN, 100)
        pwm.start(0)
        return pwm

def setMotorControl(pwm, INA, INB, speed, stat):
        pwm.ChangeDutyCycle(speed)

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