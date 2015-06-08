import RPi.GPIO as GPIO
import cameraController as camera
import imageConvert as convert
from scipy import misc
import numpy as np
from LCDController import LCDController

GPIO.setmode(GPIO.BCM)

BTN_PIN = 23

lcd = LCDController(18,24,25,17,22)

GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def doTakeAndSavePicture(channel):
	print "Taking picture"
	image = camera.takePicture()
        bitImage = convert.convertImage(image)
        asciiImage = convert.asciiize(bitImage)
        image.save("orig.png")
        misc.imsave("bit.png", bitImage.astype(np.uint8)*255)
        misc.imsave("ascii.png", asciiImage.astype(np.uint8)*255)
	print "Finished!"

def doTakeAndDisplayPicture(channel):
	print "Taking picture"
	image = camera.takePicture()
	bitImage = convert.convertImage(image)
	lcd.displayImage(bitImage)
	print "Finished!"

try:
	lcd.begin(0x18)
	GPIO.add_event_detect(BTN_PIN, GPIO.RISING, callback=doTakeAndDisplayPicture, bouncetime=50)
	raw_input("Camera Ready! Press Enter to exit.\n")
finally:
	lcd.close()
	GPIO.cleanup()
