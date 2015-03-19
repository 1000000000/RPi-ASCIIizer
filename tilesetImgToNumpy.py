import numpy as np
from imageConvert import TILE_WIDTH, TILE_HEIGHT, REDUNDANT_TILES
import imageConvert as convert
from PIL import Image

'''
Converts a black and white (not grayscale) image of the tileset to a NumPy array formatted the proper
way for the imageConvert program and saves the array to a file.
'''
def convertToNumpy(tileset):
	tilesetSize = (tileset.size[0]/TILE_WIDTH, tileset.size[1]/TILE_HEIGHT)
	tilesetArray = convert.cropImage(np.array(tileset.getdata()).astype(bool).reshape((tileset.size[1],tileset.size[0])))[0]
	newArray = np.empty((TILE_WIDTH*TILE_HEIGHT,tilesetArray.shape[0]-len(REDUNDANT_TILES)), dtype=bool)
	for p in range(TILE_WIDTH*TILE_HEIGHT):
		offset = 0
		for t in range(tilesetArray.shape[0]):
			if not t in REDUNDANT_TILES:
				newArray[p,t-offset] = tilesetArray[t].flat[p]
			else:
				offset += 1
	np.save("resources/tileset.npy", newArray)

if __name__ == "__main__":
	convertToNumpy(Image.open("resources/tileset.png").convert("1"))
