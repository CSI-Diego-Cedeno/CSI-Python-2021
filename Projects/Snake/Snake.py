import pygame
pygame.init() #This initializes all the imported pygame modules
dis=pygame.display.set_mode((400,300)) # Sets the dimensions for the game 

pygame.display.set_caption('Snake game by Edureka') #Will see this message on the display screen

#Here are th colors used, the 0 is black and the 255 is white
blue=(0, 0, 255) 
red=(255, 0, 0)

game_over=False 
while not game_over:
    for event in pygame.event.get(): #Returns all the actions 
        if event.type==pygame.QUIT: #Here QUIT closes or exits the game
            game_over=True
    
    pygame.draw.rect(dis, blue, [200, 150, 10, 10]) #This function draws the snake as a rectangle with color and size
    pygame.display.update() #Here it updates the screen
 
pygame.quit() 
quit() #This uninitialize everything