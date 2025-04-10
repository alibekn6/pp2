import pygame
import time
import math
pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Clock")


background = pygame.image.load("images/clock.png")

background = pygame.transform.scale(background, (width, height))

center_x = width // 2
center_y = height // 2
second_hand_length = min(width, height) // 3
minute_hand_length = min(width, height) // 3.5
hour_hand_length = min(width, height) // 4.5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min


    second_angle = math.radians(seconds * 6 - 90)  
    minute_angle = math.radians(minutes * 6 + seconds * 0.1 - 90)  

    screen.fill((255, 255, 255))
    
    screen.blit(background, (0, 0))
    
    minute_x = center_x + minute_hand_length * math.cos(minute_angle)
    minute_y = center_y + minute_hand_length * math.sin(minute_angle)
    pygame.draw.line(screen, (0, 0, 0), (center_x, center_y), (minute_x, minute_y), 4)
    

    second_x = center_x + second_hand_length * math.cos(second_angle)
    second_y = center_y + second_hand_length * math.sin(second_angle)
    pygame.draw.line(screen, (255, 0, 0), (center_x, center_y), (second_x, second_y), 4)
    
    pygame.draw.circle(screen, (0, 0, 0), (center_x, center_y), 6)
    

    pygame.display.flip()
    
    time.sleep(0.1)

pygame.quit()