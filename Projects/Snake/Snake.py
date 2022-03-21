import pygame
pygame.init() #This initializes all the imported pygame modules
dis=pygame.display.set_mode((400,300)) # Sets the dimensions for the game 
pygame.display.update() #Here it updates the screen
pygame.display.set_caption('Snake game by Edureka') #Will see this message on the display screen
game_over=False 
while not game_over:
    for event in pygame.event.get(): #Returns all the actions 
        if event.type==pygame.QUIT: #Here QUIT closes or exits the game
            game_over=True
 
pygame.quit() 
quit() #This uninitialize everything