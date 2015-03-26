import numpy as np
from imageConvert import TILE_WIDTH, TILE_HEIGHT, TILESET_FILE, TILESET_IMAGE
import imageConvert as convert
from PIL import Image

REDUNDANT_TILES = [8, 10, 32, 220, 222, 223, 255]

'''
Converts a black and white (not grayscale) image of the tileset to a NumPy array formatted the proper
way for the imageConvert program and saves the array to a file.
'''
def convertToNumpy(tileset):
	tilesetSize = (tileset.size[0]/TILE_WIDTH, tileset.size[1]/TILE_HEIGHT)
	tilesetArray = convert.cropImage(np.array(tileset.getdata()).astype(bool).reshape((tileset.size[1],tileset.size[0])))[0]
	np.delete(tilesetArray, REDUNDANT_TILES, axis=0)
	np.save(TILESET_IMAGE, tilesetArray)
	newArray = np.empty((TILE_WIDTH*TILE_HEIGHT,tilesetArray.shape[0]), dtype=bool)
	for p in range(TILE_WIDTH*TILE_HEIGHT):
		for t in range(tilesetArray.shape[0]):
			newArray[p,t] = tilesetArray[t].flat[p]
	np.save(TILESET_FILE, newArray)

if __name__ == "__main__":
	convertToNumpy(Image.open("resources/tileset.png").convert("1"))
