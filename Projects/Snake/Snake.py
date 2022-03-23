import pygame
import time
import random

#This initializes all the imported pygame modules
pygame.init() 

#Here are th colors used, the 0 is black and the 255 is white
white = (255, 255, 255)
black = (0, 0, 0)
red=(255, 0, 0)
blue = (0, 0, 255)

#Dimensions of the game
dis_width = 800
dis_height = 600

# Sets the dimensions for the game 
dis=pygame.display.set_mode((dis_width, dis_width)) 
#Will see this message on the display screen
pygame.display.set_caption('Snake game by Edureka') 

#This is used to keep time of the game
clock = pygame.time.Clock()
snake_block = 10
#The speed that the snake will have
snake_speed = 30

#font style for message
font_style = pygame.font.SysFont(None, 30)

#This function creates the message that will appear at game over and it creates size, color, and position of the text
def message (msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/3, dis_height/3])

#Creating a function for the game to start until it is over or closed
def gameLoop():
    game_over = False 
    game_close = False

    #The defined variables are width and height divided by 2
    x1 = dis_width/2
    y1 = dis_height/2

    #These are variables that have the values of x and y coordinates
    x1_change = 0
    y1_change = 0

    #Here it places the food on random locations of x and y coordinates
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

    #creates and starts the loop
    while not game_over:
        
        while game_close == True:
            dis.fill(white) 
            #Here it gives you the message that you lost and it updates it on the display in red
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            #Here it checks for the event that is occuring on pygame
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop() #restarts game

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
       
        #if x1 or y1 increase the change also increases
        x1 += x1_change
        y1 += y1_change

        #fills the display with the color
        dis.fill(white)


        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block]) 
        #This function draws the snake as a rectangle with color and size
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block]) 
        #Here it updates the screen
        pygame.display.update() 
        
        #Each time the snake crosses over the food it will print this message
        if x1 == foodx and y1 == foody:
            print("Yummy!!")   
        #Here the clock keeps the snake speed 
        clock.tick(snake_speed)


    #Here it quits the game
    pygame.quit() 
    #Quits all
    quit() 

#Starts the game all over 
gameLoop()