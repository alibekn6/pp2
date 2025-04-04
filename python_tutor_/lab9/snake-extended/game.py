import pygame
import time
import random

snake_speed = 10

# Window size
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Custom Caption')
game_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

# food disappear event
FOOD_DIS = pygame.USEREVENT + 1
pygame.time.set_timer(FOOD_DIS, 10000)

def generate_fruit_position():
    new_position = [random.randrange(1, (SCREEN_WIDTH//10)) * 10, 
                    random.randrange(1, (SCREEN_HEIGHT//10)) * 10]
    while new_position in snake_body:
        new_position = [random.randrange(1, (SCREEN_WIDTH//10)) * 10, 
                          random.randrange(1, (SCREEN_HEIGHT//10)) * 10]
    return new_position

# fruit position
fruit_position = generate_fruit_position()
fruit_weight = 1 # fruit weight
fruit_spawn = True

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0

# initial level
level = 1

fruits_eaten = 0

# displaying Score function
def show_level(choice, color, font, size):
  
    # creating font object score_font
    level_font = pygame.font.SysFont(font, size)
    
    # create the display surface object 
    # score_surface
    level_surface = level_font.render('Level : ' + str(level), True, color)
    
    # displaying text
    game_window.blit(level_surface, (SCREEN_WIDTH-150, 0))

# displaying Score function
def show_score(choice, color, font, size):
  
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
    
    # create the display surface object 
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
    
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
    
    # displaying text
    game_window.blit(score_surface, score_rect)

# game over function
def game_over():
  
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
    
    # creating a text surface on which text 
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
    
    # create a rectangular object for the text 
    # surface object
    game_over_rect = game_over_surface.get_rect()
    
    # setting position of the text
    game_over_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/4)
    # game_over_rect.centerx = 500
    
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    # after 2 seconds we will quit the program
    time.sleep(2)
    
    # deactivating pygame library
    pygame.quit()
    
    # quit the program
    quit()

# Main Function
while True:
    
    # handling key events
    for event in pygame.event.get():
        if event.type == FOOD_DIS:
              fruit_position = generate_fruit_position()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
    

    # If two keys pressed simultaneously
    # we don't want snake to move into two 
    # directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        fruits_eaten += 1
        score += 10 * level * fruit_weight
        fruit_weight = 1
        fruit_spawn = False
    else:
        snake_body.pop()
    
    if not fruit_spawn and fruits_eaten % 3 == 0:
        level += 1
        snake_speed = 10 * level
        fruit_weight = 2

    if not fruit_spawn:
        fruit_position = generate_fruit_position()
        
    fruit_spawn = True
    game_window.fill(black)
    
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, (127 * fruit_weight, 0, 0, 255), pygame.Rect( # color if weight
        fruit_position[0], fruit_position[1], 10, 10))

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > SCREEN_WIDTH-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > SCREEN_HEIGHT-10:
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # displaying score continuously
    show_score(1, blue, 'times new roman', 35)
    show_level(1, blue, 'times new roman', 35)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)