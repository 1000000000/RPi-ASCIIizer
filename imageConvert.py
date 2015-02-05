import numpy as np
from scipy import ndimage
from PIL import Image
from math import copysign

TILE_WIDTH = 6
TILE_WIDTH = 8

#Note that this takes a Pillow Image and returns a NumPy boolean array
def convertImage(image):
	return np.array(image.resize((128, 64), Image.ANTIALIAS).convert("1").getdata()).reshape((64,128)).astype(bool)



# Takes a 2D NumPy array and returns a 8x6x?? NumPy array
def cropImage(npImg):
#	import pdb; pdb.set_trace()
        numRow = npImg.shape[0]
        extraRow = (numRow % 8)//2
        rowToRemove = range(extraRow) + range(numRow - extraRow, numRow)
        if (numRow % 2) == 1:
		#print type(rowToRemove)
                rowToRemove.append(extraRow)
        npImg = np.delete(npImg, rowToRemove, 0)

        numCol = npImg.shape[1]
        extraCol = (numCol % 6)//2
        colToRemove = range(extraCol) + range(numCol - extraCol, numCol)
        if (numCol % 2) == 1:
                colToRemove.append(extraCol)
        npImg = np.delete(npImg, colToRemove, 1)
	newImage = np.empty((npImg.size//48,8,6), dtype=bool)
	i = 0
	for r in range(0, npImg.shape[0], 8):
		for c in range(0, npImg.shape[1], 6):
			newImage[i] = npImg[r:r+8,c:c+6]
			i += 1
	return newImage, npImg.shape

# I wanted to put this at the top but no! Python wouldn't let me
tileset = cropImage(np.array(Image.open("resources/tileset.png").convert("1").getdata()).reshape((128,96)).astype(bool))[0] # This will be a boolean array array

def asciiize(npImg):
	npImg = cropImage(npImg)
	image = npImg[0]
	newImage = np.empty(image.shape, dtype=bool)
#	import pdb; pdb.set_trace()
	for b in range(0,image.shape[0]):
		print "Starting block " + str(b) + "/" + str(image.shape[0])
		goodTile = tileset[0]
		high = 0
		for tile in tileset:
			sim = getSimilarity(image[b],tile)
			if abs(sim) > abs(high):
				high = sim
				goodTile = tile
		newImage[b] = np.logical_xor(goodTile, np.sign(high) < 0)
	return newImage.reshape(npImg[1][0],npImg[1][1])

def getSimilarity(img,ascii):
	if img.shape != ascii.shape:
		print "Image and tile are not the same size!"
		return 0
	count = 0
	for i in range(img.size):
		if img.flat[i] == ascii.flat[i]:
			count += 1
		else:
			count -= 1
	return count

if __name__ == "__main__":
	newImage = convertImage(Image.open("resources/image.png"))
	asciiImage = asciiize(newImage)
	Image.fromarray(newImage, mode="1").save("bit.png")
	Image.fromarray(asciiImage, mode="1").save("ascii.png")