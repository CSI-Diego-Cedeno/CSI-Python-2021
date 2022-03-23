import pygame

#This initializes all the imported pygame modules
pygame.init() 

#Here are th colors used, the 0 is black and the 255 is white
white = (255, 255, 255)
black = (0, 0, 0)
red=(255, 0, 0)

# Sets the dimensions for the game 
dis=pygame.display.set_mode((800,600)) 
#Will see this message on the display screen
pygame.display.set_caption('Snake game by Edureka') 

game_over=False 

x1 = 300
y1 = 300

#These are variables that have the values of x and y coordinates
x1_change = 0
y1_change = 0

#This is used to keep time of the game
clock = pygame.time.Clock()

while not game_over:
    #Returns all the actions 
    for event in pygame.event.get(): 
        #Here QUIT closes or exits the game
        if event.type == pygame.QUIT: 
            game_over = True
        #This is the KEYDOWN class of Pygame which has different key events that can move the snake in different directions.
        if event.type == pygame.KEYDOWN: 
            #Moves the snake to the left 
            if event.key == pygame.K_LEFT: 
                x1_change = -10
                y1_change = 0
            #Moves the snake to the right
            elif  event.key == pygame.K_RIGHT: 
                 x1_change = 10
                 y1_change = 0
            #Moves the snake up
            elif  event.key == pygame.K_UP: 
                 y1_change = -10
                 x1_change = 0
            #Moves the snake down
            elif  event.key == pygame.K_DOWN: 
                 y1_change = 10
                 x1_change = 0

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    #This function draws the snake as a rectangle with color and size
    pygame.draw.rect(dis, black, [x1, y1, 10, 10]) 
    #Here it updates the screen
    pygame.display.update() 

    clock.tick(30)

#Here it quits the game
pygame.quit() 
#Quits all
quit() 