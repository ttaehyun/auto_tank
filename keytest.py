# -*- coding: utf-8 -*-
import ASUS.GPIO as GPIO
import curses

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

def keymap(screen):
	screen.clear()
	screen.refresh()
	try:
		while True :

			curses.halfdelay(2) # 2/10s 
			key = screen.getch()
			#key 값이 입력이 없으면 계속 위 코드에서 정지해서 밑에게 실행이 안된거임
			# 0으로 반환하는 그런걸 찾아야할듯
			if key == curses.KEY_UP:
				Left_track.setMotor(60, Forward)
				Right_track.setMotor(60,Forward)
			elif key == curses.KEY_DOWN:
				Left_track.setMotor(60,Backward)
				Right_track.setMotor(60,Backward)
			elif key == curses.KEY_LEFT:
				Left_track.setMotor(60,Backward)
				Right_track.setMotor(60,Forward)
			elif key == curses.KEY_RIGHT:
				Left_track.setMotor(60, Forward)
				Right_track.setMotor(60, Backward)
			elif key == 119:
				#주포 윗방향
				gun_tilt.setMotor(60, Forward)
			elif key == 115:
				#주포 아랫방향
				gun_tilt.setMotor(60, Backward)
			elif key == 97:
				#포탑 왼쪽회전
				turret_rotation.setMotor(100, Forward)
			elif key == 100:
				#포탑 오른쪽회전
				turret_rotation.setMotor(100, Backward)
			elif key == 114:
				#장전
				gun_reload.setMotor(100, Forward)
			else:
				Left_track.setMotor(0, Stop)
				Right_track.setMotor(0,Stop)
				gun_reload.setMotor(0,Stop)
				gun_tilt.setMotor(0, Stop)
				turret_rotation.setMotor(0, Stop)
				
	except KeyboardInterrupt:
		print("\nCtrl c 중지")

curses.wrapper(keymap)

GPIO.cleanup() 