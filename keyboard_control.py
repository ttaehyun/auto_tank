# -*- coding: utf-8 -*-
import ASUS.GPIO as GPIO
import curses

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# 전후 좌우 모터상태
Forward = 0
Backward = 1
Stop = 2
#모터 채널
CH1 = 0
CH2 = 1
CH3 = 2
CH4 = 3
#PIN 입출력 설정
OUTPUT = 1
INPUT = 0
#PIN 설정
HIGH = 1
LOW = 0

#PWM PIN (궤도)
ENA = 32
ENB = 33
#GPIO PIN
IN1 = 38
IN2 = 36
IN3 = 37
IN4 = 35

#PWM PIN (포탑, 주포)
ENC = 24 #포탑
END = 19 #주포
#GPIO PIN
IN5 = 16 #포탑
IN6 = 22 #포탑
IN7 = 21 #주포
IN8 = 23 #주포

#PWM PIN (장전)
ENE = 8
#GPIO PIN
IN9 = 10
IN10 = 12

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
               setMotorControl(Left_track, IN1, IN2, speed, stat)
        elif ch == CH2: 
               setMotorControl(Right_track, IN3, IN4, speed, stat)
        elif ch == CH3:
               setMotorControl(turret_rotation, IN5, IN6, speed, stat)

#왼쪽 궤도
Left_track = setPinConfig( ENA, IN1, IN2)
#오른쪽 궤도
Right_track = setPinConfig(ENB, IN3, IN4)
#포탑 회전
turret_rotation = setPinConfig(ENC, IN5, IN6)
#주포
gun_tilt = setPinConfig(END, IN7, IN8)
#장전
gun_reload = setPinConfig(ENE, IN9, IN10)
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