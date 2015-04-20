import picamera
import io
from PIL import Image

def takePicture():
	stream = io.BytesIO()
	with picamera.PiCamera() as camera:
		camera.resolution = (1024, 768)
		camera.capture(stream, format='png')
	stream.seek(0)
	return Image.open(stream)
		
if __name__ == "__main__":
	import imageConvert as convert
	from scipy import misc
	import numpy as np
	image = takePicture()
	bitImage = convert.convertImage(image)
        asciiImage = convert.asciiize(bitImage)
	image.save("orig.png")
        misc.imsave("bit.png", bitImage.astype(np.uint8)*255)
	misc.imsave("ascii.png", asciiImage.astype(np.uint8)*255)
