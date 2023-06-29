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
class Gpio_setting:
    def __init__(self, En, Ina, Inb):
        self.en = En
        self.ina = Ina
        self.inb = Inb
    def setPinConfig(self):
        GPIO.setup(self.en, GPIO.OUT)
        GPIO.setup(self.ina, GPIO.OUT)
        GPIO.setup(self.inb, GPIO.OUT)
        pwm = GPIO.PWM(self.en, 100)
        pwm.start(0)
        return pwm
class Motor(Gpio_setting):
      def __init__(self,En, Ina, Inb):
          super().__init__(En, Ina, Inb)
          self.speed = 0
          self.stat = 0

      def setMotor(self, pwm, speed, stat):
          pwm.ChangeDutyCycle(speed)
          if stat == Forward:
               GPIO.output(self.Ina, LOW)
               GPIO.output(self.Inb, HIGH)
          elif stat == Backward:
               GPIO.output(self.Ina, HIGH)
               GPIO.output(self.Inb, LOW)
          elif stat == Stop:
               GPIO.output(self.Ina, LOW)
               GPIO.output(self.Inb, LOW)

Left_track = Motor(32, 38, 26)
Right_track = Motor(33, 37, 35)
turret_rotation = Motor(24, 16, 22)
gun_tilt = Motor(19, 21, 23)
gun_reload = Motor(27, 29, 31)


GPIO.cleanup()