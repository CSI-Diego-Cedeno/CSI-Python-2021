import pygame

pygame.init() #This initializes all the imported pygame modules

#Here are th colors used, the 0 is black and the 255 is white
white = (255, 255, 255)
black = (0, 0, 0)
red=(255, 0, 0)

dis=pygame.display.set_mode((800,600)) # Sets the dimensions for the game 
pygame.display.set_caption('Snake game by Edureka') #Will see this message on the display screen

game_over=False 

x1 = 300
y1 = 300

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get(): #Returns all the actions 
        if event.type == pygame.QUIT: #Here QUIT closes or exits the game
            game_over = True
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT: #The snake moves to the left 
                x1_change = -10
                y1_change = 0
            elif  event.key == pygame.K_RIGHT:
                 x1_change = 10
                 y1_change = 0
            elif  event.key == pygame.K_UP:
                 y1_change = -10
                 x1_change = 0
            elif  event.key == pygame.K_DOWN:
                 y1_change = 10
                 x1_change = 0

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, 10, 10]) #This function draws the snake as a rectangle with color and size

    pygame.display.update() #Here it updates the screen

    clock.tick(30)
 
pygame.quit() 
quit() #This uninitialize everything