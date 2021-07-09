import pygame 
import game_confi as gc

from pygame import display, event, image
from time import sleep
from animal import Animal

def find_index_from_xy(x, y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    index = row * gc.NUM_TILES_SIDE + col
    return row, col, index

pygame.init()
display.set_caption('My Game')
screen = display.set_mode((gc.SCREEN_SIZE, gc.SCREEN_SIZE))#it is a surface object on top of which our game will run ,
# all the images will also be surface objects.
matched = image.load('other_assets/matched.png') # pass in the path 
#to the image this returns a surface elements
#####screen.blit(matched, (0,0))# the blit() methods dispays a surface
#over another surfaace
#parametrs are the image along with the coordinates, since we want
#the image to take entire screen, we will start at 0,0 which is top left 
#corner of the screen, and this image is 512 x 512, so it takes entire space.
#although the screen is now updated, but the update is not displayed yet.

#####display.flip() #flip method helps displaying.
running = True
#instatantiate all the animal tiles that we'll be using
tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]
#i will be from 0 to 15 included which will randomly have diff. animal names and images
current_images_displayed = []

#game loop that will run for as long as running is set to True
while running:
    #pygames event module lets u get a list of all the keyboard 
    #and mouse events with the help of get function.
    #all the events fetched from the event queue will be 
    #removed from the queue and returned as a list
    current_events = event.get()

    for e in current_events:#iterates through all the fn. since
        #last get executed
	    # "event" is used to Fetch a list of all the event 
        #messages since the last time this function was called. All the fetched messages are then removed from the event queue.
        if e.type == pygame.QUIT: #QUIT is a keyword defined in pygames 
            running = False
            
         #mouse events or key events
        if e.type == pygame.KEYDOWN:  #if key is pressed
            if e.key == pygame.K_ESCAPE:   #and that key is escape
                running = False #stop running or even click on cross


        if e.type == pygame.MOUSEBUTTONDOWN: #if mouse button pressed
            mouse_x, mouse_y = pygame.mouse.get_pos() # we get position of mouse for the index
            row, col, index = find_index_from_xy(mouse_x, mouse_y)   #getting from the mouse module(we can also import this module)
            #find index is a fn. we will define.
            if index not in current_images_displayed:
                if len(current_images_displayed) > 1: #because we want 2 at a time
                    current_images_displayed = current_images_displayed[1:] + [index] #oldest element will be ignored
                else:
                    current_images_displayed.append(index) #so that image doesnt match with itself when clicked twice

    # Display animals
    screen.fill((255, 255, 255))   # set the screen have white bg, as a starting point and simply iterate over all images 

    total_skipped = 0

    for i, tile in enumerate(tiles): #for i in the numbers in tiles
        current_image = tile.image if i in current_images_displayed else tile.box
        if not tile.skip:  #if tile.skip is not set to false then display
            screen.blit(current_image, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))
        else:   # if the tile is skipped
            total_skipped += 1
            
             #iterate of    all the tile and display images
        #image will be doisplayed at diff. coordinates that is image size * no. of row or column
        #this should update the screen with all the 16 images for each tile

    display.flip()

    # Check for matches
    if len(current_images_displayed) == 2:
        idx1, idx2 = current_images_displayed
        if tiles[idx1].name == tiles[idx2].name: #if images are same.
            tiles[idx1].skip = True  #to remove that image from the grid
            tiles[idx2].skip = True
            # display matched message
            sleep(0.4)   # sleep for 400 milli secs after matched
            screen.blit(matched, (0, 0)) # to display the image that says matched
            display.flip()
            sleep(0.5) # then sleep again ,ie, pause for a while
            current_images_displayed = [] #set the list of recents to 0 so that only the last two images gets saved in it to be compared.

    if total_skipped == len(tiles):
        running = False  #stops or ends the game when everything is skipped, all the images are grayed.

print('Goodbye!')
