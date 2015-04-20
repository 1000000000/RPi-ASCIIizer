import os.path
import numpy as np
from scipy import misc
from PIL import Image
from math import copysign

TILE_WIDTH = 6
TILE_HEIGHT = 8

TILESET_FILE = "resources/tileset.npy"
TILESET_IMAGE = "resources/tileset-img.npy"

# Make sure the tileset array file exists. If not create it from the tileset image
def loadTileset():
	if not os.path.isfile(TILESET_FILE) or not os.path.isfile(TILESET_IMAGE):
		import tilesetImgToNumpy as toNumpy
		toNumpy.convertToNumpy("resources/tileset.png")
	tileset = np.load(TILESET_FILE) # This will be a boolean array array
	tilesetImg = np.load(TILESET_IMAGE) # This will be a boolean array array array (An array of tiles which are 2D boolean array)
	return tileset, tilesetImg

#Note that this takes a Pillow Image and returns a NumPy boolean array of the image scaled to fit on the LCD screen
def convertImage(image):
	return np.array(image.resize((128, 64), Image.ANTIALIAS).convert("1").getdata()).reshape((64,128)).astype(bool)


# Takes a 2D NumPy array and returns a 8x6x?? NumPy array
def cropImage(npImg):
        numRow = npImg.shape[0]
        extraRow = (numRow % TILE_HEIGHT)//2
        rowToRemove = range(extraRow) + range(numRow - extraRow, numRow)
        if (numRow % 2) == 1:
		#print type(rowToRemove)
                rowToRemove.append(extraRow)
        npImg = np.delete(npImg, rowToRemove, 0)

        numCol = npImg.shape[1]
        extraCol = (numCol % TILE_WIDTH)//2
        colToRemove = range(extraCol) + range(numCol - extraCol, numCol)
        if (numCol % 2) == 1:
                colToRemove.append(extraCol)
        npImg = np.delete(npImg, colToRemove, 1)
	newImage = np.empty((npImg.size//(TILE_WIDTH*TILE_HEIGHT),TILE_HEIGHT,TILE_WIDTH), dtype=bool)
	i = 0
	for r in range(0, npImg.shape[0], TILE_HEIGHT):
		for c in range(0, npImg.shape[1], TILE_WIDTH):
			newImage[i] = npImg[r:r+TILE_HEIGHT,c:c+TILE_WIDTH]
			i += 1
	return newImage, npImg.shape


def asciiize(npImg):
	tileset, tilesetImg = loadTileset()
	npImg = cropImage(npImg)
	image = npImg[0]
	newImage = np.empty(image.shape, dtype=bool)
	for b in range(image.shape[0]):
		print "Starting block " + str(b) + "/" + str(image.shape[0])
		acc = np.full(tileset.shape[1], -2*np.sum(image[b]) + image[b].size)
		for i in range(image[b].size):
			acc += 2*tileset[i]*(2*image[b].flat[i] - 1)
		bestTile = np.argmax(np.absolute(acc))
		newImage[b] = np.logical_xor(tilesetImg[bestTile], np.sign(acc[bestTile]) < 0)
	doneImage = np.empty(npImg[1], dtype=bool)
	i = 0
	for r in range(0, npImg[1][0], TILE_HEIGHT):
		for c in range(0, npImg[1][1], TILE_WIDTH):
			doneImage[r:r+TILE_HEIGHT,c:c+TILE_WIDTH] = newImage[i]
			i += 1
	return doneImage


if __name__ == "__main__":
	newImage = convertImage(Image.open("resources/image.png"))
	asciiImage = asciiize(newImage)
	misc.imsave("bit.png", newImage.astype(np.uint8)*255) # saving using scipy cause array to PIL image conversion is weird
	misc.imsave("ascii.png", asciiImage.astype(np.uint8)*255)
