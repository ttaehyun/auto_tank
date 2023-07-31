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

def keyboard_control(screen):
	key = screen.getch()
	if key == curses.KEY_UP:
		return "up"
	elif key == curses.KEY_DOWN:
		return "down"
	elif key == curses.KEY_LEFT:
		return "left"
	elif key == curses.KEY_RIGHT:
		return "right"
	else:
		return "stop"
	
def keymap(screen):
	screen.clear()
	screen.refresh()
	try:
		while True :
			test = keyboard_control(screen)		
			
			#key 값이 입력이 없으면 계속 위 코드에서 정지해서 밑에게 실행이 안된거임
			# 0으로 반환하는 그런걸 찾아야할듯
			if test == "up":
				Left_track.setMotor(60, Forward)
				Right_track.setMotor(60,Forward)
			elif test == "down":
				Left_track.setMotor(60,Backward)
				Right_track.setMotor(60,Backward)
			elif test == "left":
				Left_track.setMotor(60,Backward)
				Right_track.setMotor(60,Forward)
			elif test == "right":
				Left_track.setMotor(60, Forward)
				Right_track.setMotor(60, Backward)
			
				
	except KeyboardInterrupt:
		print("\nCtrl c 중지")

curses.wrapper(keymap)

GPIO.cleanup() 