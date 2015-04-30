import RPi.GPIO as GPIO
import cameraController as camera
import imageConvert as convert
from scipy import misc
import numpy as np

GPIO.setmode(GPIO.BCM)

BTN_PIN = 23

GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def doTakePicture(channel):
	print "Taking picture"
	image = camera.takePicture()
        bitImage = convert.convertImage(image)
        asciiImage = convert.asciiize(bitImage)
        image.save("orig.png")
        misc.imsave("bit.png", bitImage.astype(np.uint8)*255)
        misc.imsave("ascii.png", asciiImage.astype(np.uint8)*255)
	print "Finished!"

GPIO.add_event_detect(BTN_PIN, GPIO.RISING, callback=doTakePicture, bouncetime=50)

print "Using NumPy version: " + np.__version__ + " at " + np.__file__
raw_input("Camera Ready! Press Enter to exit.\n")

GPIO.cleanup()
