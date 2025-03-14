import pygame
import random

pygame.init()
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
done = False

ball_x = (WIDTH // 2)
ball_y = (HEIGHT // 2)
ball_radius = 25
ball_speed_x = 20
ball_speed_y = 20
ball_color = (101, 202, 110)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # ball_x += ball_speed_x
    # ball_y += ball_speed_y

    # if ball_x + ball_radius > WIDTH or ball_x - ball_radius < 0:
    #     ball_speed_x = -ball_speed_x
    # if ball_y + ball_radius > HEIGHT or ball_y - ball_radius < 0:
    #     ball_speed_y = -ball_speed_y

    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT] and ball_x - ball_radius > 0:
        ball_x -= ball_speed_x
    if keys[pygame.K_RIGHT] and ball_x + ball_radius < WIDTH:
        ball_x += ball_speed_x
    if keys[pygame.K_UP] and ball_y - ball_radius > 0:
        ball_y -= ball_speed_y
    if keys[pygame.K_DOWN] and ball_y + ball_radius < HEIGHT:
        ball_y += ball_speed_y

    print(ball_x, ball_y)
    screen.fill((255,255,255))

    pygame.draw.circle(screen, ball_color, (int(ball_x), int(ball_y)), ball_radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


# Draw circle - a red ball of size 50 x 50 (radius = 25) on white background.
#  When user presses Up, Down, Left, Right arrow keys on keyboard, 
# the ball should move by 20 pixels in the direction of pressed key. 
# The ball should not leave the screen, i.e. user input that leads the ball to
#  leave of the screen should be ignored