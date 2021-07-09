import os

IMAGE_SIZE = 128  #for each tile
SCREEN_SIZE = 512  #4 images in total
NUM_TILES_SIDE =4 
NUM_TILES_TOTAL = 16
MARGIN = 4 #b/w two images from each side

ASSET_DIR = 'assets'
ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3:].lower() == 'png']
#loop over all the files and check last 3 characters
assert len(ASSET_FILES)== 8 #since we have 8 files (as we know)
#we are making sure that it loops over all the 8 files.
