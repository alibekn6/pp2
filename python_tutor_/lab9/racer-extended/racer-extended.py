# Imports
import sys
import pygame
from pygame.locals import *
import random, time


# Init
pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()
# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINSCORE = 0

# Setting up FONTS
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("assets/AnimatedStreet.png")

# Creating a white screen
DISPLAYSURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURFACE.fill(WHITE)
pygame.display.set_caption("Gameeee")




class Coin(pygame.sprite.Sprite):
    Weight = 1
    image = pygame.image.load('assets/coin.png')
    def __init__(self, image, weight):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
        self.Weight = weight
    
    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def reset(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)



# Enemy class (Car)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.bottom > 800):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


# Player class (Car that we drive)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
             self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
             self.rect.move_ip(0,5)
         

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-10, 0)
        
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(10, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)  



# Object of classes
P = Player()
E = Enemy()
C1 = Coin(pygame.image.load('assets/coin.png'), 1)
C3 = Coin(pygame.image.load('assets/coin+.png'), 3)
# adding them to a group
enemies = pygame.sprite.Group()
enemies.add(E)

coins = pygame.sprite.Group()
coins.add(C1)
coins.add(C3)

all_sprites = pygame.sprite.Group()
all_sprites.add(P)
all_sprites.add(E)
all_sprites.add(C1)
all_sprites.add(C3)

# adding a new user event (unique id)
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
# every 1000 milisecond this event accurs -> which increases the speed

# main game loop
while True:
    # for loop through all events accuring
    for event in pygame.event.get():

        if event.type == INC_SPEED:
            SPEED += 0.5
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # pygame.mixer.Sound('assets/background.wav').play()


    # setting up the background 
    DISPLAYSURFACE.blit(background, (0,0))
    # showing score in the screen
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURFACE.blit(scores, (10, 10))
    scores = font_small.render(f"Coins: {COINSCORE}", True, BLACK)
    DISPLAYSURFACE.blit(scores, (SCREEN_WIDTH-100,10))
    # moves and redraws all sprites
    for entity in all_sprites:
        DISPLAYSURFACE.blit(entity.image, entity.rect)
        entity.move()
    

    # checking if collision occurs
    if pygame.sprite.spritecollideany(P, enemies):
        pygame.mixer.Sound('assets/crash.wav').play()
        time.sleep(0.5)
        
        DISPLAYSURFACE.fill(RED)
        DISPLAYSURFACE.blit(game_over, (30, 250))
    
        pygame.display.update()

        # if accurs deleting entities from all_sprites
        for entity in all_sprites:
            entity.kill()

        time.sleep(2)
        pygame.quit()
        sys.exit()

    collision = pygame.sprite.spritecollideany(P, coins)

    if collision:
        COINSCORE += collision.Weight
        SPEED += 0.5
        collision.reset()


    pygame.display.update()
    FramePerSec.tick(FPS)