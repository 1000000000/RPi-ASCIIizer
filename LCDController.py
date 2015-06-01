# We are dealing with an Adafruit ST7565 LCD here
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

class LCDController:
	#Various constants for commands to be sent to the LCD screen
	CMD_DISPLAY_OFF = 0xAE
	CMD_DISPLAY_ON = 0xAF

	CMD_SET_DISP_START_LINE = 0x40
	CMD_SET_PAGE = 0xB0

	CMD_SET_COLUMN_UPPER = 0x10
	CMD_SET_COLUMN_LOWER = 0x00

	CMD_SET_ADC_NORMAL = 0xA0
	CMD_SET_ADC_REVERSE = 0xA1

	CMD_SET_DISP_NORMAL = 0xA6
	CMD_SET_DISP_REVERSE = 0xA7

	CMD_SET_ALLPTS_NORMAL = 0xA4
	CMD_SET_ALLPTS_ON = 0xA5
	CMD_SET_BIAS_9 = 0xA2
	CMD_SET_BIAS_7 = 0xA3

	CMD_RMW = 0xE0
	CMD_RMW_CLEAR = 0xEE
	CMD_INTERNAL_RESET = 0xE2
	CMD_SET_COM_NORMAL = 0xC0
	CMD_SET_COM_REVERSE = 0xC8
	CMD_SET_POWER_CONTROL = 0x28
	CMD_SET_RESISTOR_RATIO = 0x20
	CMD_SET_VOLUME_FIRST = 0x81
	CMD_SET_VOLUME_SECOND = 0
	CMD_SET_STATIC_OFF = 0xAC
	CMD_SET_STATIC_ON = 0xAD
	CMD_SET_STATIC_REG = 0x0
	CMD_SET_BOOSTER_FIRST = 0xF8
	CMD_SET_BOOSTER_234 = 0
	CMD_SET_BOOSTER_5 = 1
	CMD_SET_BOOSTER_6 = 3
	CMD_NOP = 0xE3
	CMD_TEST = 0xF0

	def __init__(self, sid, sclk, a0, rst, cs):
		self.sid = sid
		self.sclk = sclk
		self.a0 = a0
		self.rst = rst
		self.cs = cs

	def init(self):
		GPIO.setup(self.sid, GPIO.OUT)
		GPIO.setup(self.sclk, GPIO.OUT)
		GPIO.setup(self.a0, GPIO.OUT)
                GPIO.setup(self.rst, GPIO.OUT)
                GPIO.setup(self.cs, GPIO.OUT)
		if (self.cs > 0):
			GPIO.output(self.cs, False)
		GPIO.output(self.rst, False)
		time.sleep(0.5)
		GPIO.output(self.rst, True)
		
		lcdCommand(CMD_SET_BIAS_7)
		lcdCommand(CMD_SET_ADC_NORMAL)
		lcdCommand(CMD_SET_COM_NORMAL)
		lcdCommand(CMD_SET_DISP_START_LINE)
		
		lcdCommand(CMD_SET_POWER_CONTROL | 0x4)
		time.sleep(0.05)
		
		lcdCommand(CMD_SET_POWER_CONTROL | 0x6)
		time.sleep(0.05)
		
		lcdCommand(CMD_SET_POWER_CONTROL | 0x7)
		time.sleep(0.01)
		
		lcdCommand(CMD_SET_RESISTOR_RATIO | 0x6)
	
	def begin(self, contrast)
		init()
		lcdCommand(CMD_DISPLAY_ON)
		lcdCommand(CMD_SET_ALLPTS_NORMAL)
		lcdSetBrightness(contrast)
	
	def writeToLCD(data):
		for i in range(7, -1, -1):
			GPIO.output(self.sid, bool(data & (1 << i)))
			GPIO.output(self.sclk, True)
			GPIO.output(self.sclk, False)
	
	def lcdCommand(command):
		GPIO.output(self.a0, False)
		writeToLCD(command)
	
	def lcdData(data):
		GPIO.output(self.a0, True)
		writeToLCD(data)
	
	def lcdSetBrightness(contrast):
		lcdCommand(CMD_SET_VOLUME_FIRST)
		lcdCommand(CMD_SET_VOLUME_SECOND | (contrast & 0x3f))
