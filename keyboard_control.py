# -*- coding: utf-8 -*-
import ASUS.GPIO as GPIO
import curses

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# 전후 좌우 모터상태
Forward = 0
Reverse = 1
Stop = 2
#모터 채널
CH1 = 0
CH2 = 1
CH3 = 2
CH4 = 3
CH5 = 4
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
ENE = 27
#GPIO PIN
IN9 = 29
IN10 = 31

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
        elif stat == Reverse:
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
        elif ch == CH4:
                setMotorControl(gun_tilt, IN7, IN8, speed, stat)
        elif ch == CH5:
                setMotorControl(gun_reload, IN9, IN10, speed, stat)
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
                        
                        # setMotor(CH1, 0, Forward)
                        # setMotor(CH2, 0, Forward)
                        print(key)
                        key = screen.getch()
                        #key 값이 입력이 없으면 계속 위 코드에서 정지해서 밑에게 실행이 안된거임
                        # 0으로 반환하는 그런걸 찾아야할듯
                        if key == curses.KEY_UP:
                                setMotor(CH1, 100, Forward)
                                setMotor(CH2, 100, Forward)
                                print("윗키")
                        elif key == curses.KEY_DOWN:
                                setMotor(CH1, 100, Reverse)
                                setMotor(CH2, 100, Reverse)
                                print("아랫키")
                        elif key == curses.KEY_LEFT:
                                setMotor(CH1, 50, Forward)
                                setMotor(CH2, 50, Reverse)
                                print("왼쪽키")
                        elif key == curses.KEY_RIGHT:
                                setMotor(CH1, 50, Reverse)
                                setMotor(CH2, 50, Forward)
                                print("오른쪽키")
                        elif key == curses.KEY_HOME:
                                setMotor(CH4, 50, Forward)
                                print("ch41키")
                        elif key == curses.KEY_END:
                                setMotor(CH4, 50, Reverse)
                                print("ch42키")
                        elif key == curses.KEY_F9:
                                setMotor(CH3, 50, Forward)
                                print("ch31키")
                        elif key == curses.KEY_F10:
                                setMotor(CH3, 50, Reverse)
                                print("ch32키")
                        elif key == curses.KEY_F11:
                                setMotor(CH5, 50, Forward)
                                print("ch5키")
                        else:
                                setMotor(CH1, 0, Stop)
                                setMotor(CH2, 0, Stop)
                                print("else 실행")
                        print("if문 빠져나옴")
                        print(key)
                        #key = ""
                        screen.refresh()
        except KeyboardInterrupt:
                print("\nCtrl c 중지")

curses.wrapper(keymap)

GPIO.cleanup() 