import pygame
import time

#This initializes all the imported pygame modules
pygame.init() 

#Here are th colors used, the 0 is black and the 255 is white
white = (255, 255, 255)
black = (0, 0, 0)
red=(255, 0, 0)

#Dimensions of the game
dis_width = 800
dis_height = 600

# Sets the dimensions for the game 
dis=pygame.display.set_mode((dis_width, dis_width)) 
#Will see this message on the display screen
pygame.display.set_caption('Snake game by Edureka') 

game_over=False 

#the defined variables are width and height divided by 2
x1 = dis_width/2
y1 = dis_height/2

snake_block= 10

#These are variables that have the values of x and y coordinates
x1_change = 0
y1_change = 0

#This is used to keep time of the game
clock = pygame.time.Clock()
#The speed that the snake will have
snake_speed = 30

#font style for message
font_style = pygame.font.SysFont(None, 50)

#This function creates the message that will appear at game over and it creates size, color, and position of the text
def message (msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

#creates and starts the loop
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
                x1_change = -snake_block
                y1_change = 0
            #Moves the snake to the right
            elif  event.key == pygame.K_RIGHT: 
                 x1_change = snake_block
                 y1_change = 0
            #Moves the snake up
            elif  event.key == pygame.K_UP: 
                 y1_change = -snake_block
                 x1_change = 0
            #Moves the snake down
            elif  event.key == pygame.K_DOWN: 
                 y1_change = snake_block
                 x1_change = 0
    #defines limits for x and y coordinates of the snake, less or equal to the screen
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    #This function draws the snake as a rectangle with color and size
    pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block]) 
    #Here it updates the screen
    pygame.display.update() 

    #Here the clock keeps the snake speed 
    clock.tick(snake_speed)

#Here it gives you the message that you lost and it updates it on the display in red
message("You lost", red)
pygame.display.update()
time.sleep(2)

#Here it quits the game
pygame.quit() 
#Quits all
quit() 