import os
import random
import game_confi as gc
from pygame import image, transform

animals_count=dict((a,0) for a in gc.ASSET_FILES )# to keep a track of animals that we use
#this will set the values to 0 for all the keys, and the keys will be all the files from our asset files(animals pics).
def available_animals():
    return [a for a, c in animals_count.items() if c<2] #retunrs the list of all animals which are available, aie, all the keys whoseeeeeeeeee values are less than two(every im age occurs for max 2 times,ie, a pair)

class Animal:
    def __init__(self,index):
        ##from 0 to 15 inclusive based on that we will place animals on the game port
        self.index = index
        self.row = index//gc.NUM_TILES_SIDE # // to get an int
        # num of tiles side is 4 in our case, so if the index is 4, we get the row is 1

        self.col = index % gc.NUM_TILES_SIDE #index is 4, then row is 1, and col is 0, bcz we are starting our count from 0

        self.name = random.choice(available_animals()) #name will be chosen randomly from all the available names that we have

        animals_count[self.name] +=1 #whatever name that is chosen, that key value will be updates in this dictionary
        
        self.image_path = os.path.join(gc.ASSET_DIR, self.name )  #
        self.image = image.load(self.image_path)
        #in addition to the image we will aslo need a gray box, so either the image will be displayed or the box will be displayed
        #    transform the image to the right size, exclude the margin or remove the margins 
        self.image = transform.scale(self.image, (gc.IMAGE_SIZE -2*gc.MARGIN, gc.IMAGE_SIZE - 2*gc.MARGIN))
        self.box = self.image.copy() #to create the copy of this image
        self.box.fill((200,200,200)) # gray colors rgb values
        self.skip = False #if the pair is matched, we will skip printing the image or box of thet image, or will remove that image from game port
        