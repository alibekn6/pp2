import pygame
import time
import random
import psycopg2
from psycopg2 import sql
from datetime import datetime

# ========== DATABASE SETUP ========== #
conn = psycopg2.connect(
    dbname="suppliers", user="postgres", password="post667", host="localhost", port="5432"
)
cur = conn.cursor()

username = input("Enter your username: ")

cur.execute("SELECT id FROM users WHERE username = %s;", (username,))
user = cur.fetchone()

if not user:
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id;", (username,))
    user_id = cur.fetchone()[0]
    conn.commit()
    print(f"Welcome, {username}. Starting from level 1.")
    level = 1
else:
    user_id = user[0]
    cur.execute("SELECT level FROM user_scores WHERE user_id = %s ORDER BY created_at DESC LIMIT 1;", (user_id,))
    result = cur.fetchone()
    if result:
        level = result[0]
        print(f"Welcome back, {username}. Resuming at level {level}.")
    else:
        level = 1
        print(f"Welcome back, {username}. Starting from level 1.")

# ========== GAME SETTINGS ========== #
snake_speed = 10 * level
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fps = pygame.time.Clock()

snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

FOOD_DIS = pygame.USEREVENT + 1
pygame.time.set_timer(FOOD_DIS, 10000)

def generate_fruit_position():
    new_position = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10,
                    random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
    while new_position in snake_body:
        new_position = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10,
                        random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
    return new_position

fruit_position = generate_fruit_position()
fruit_weight = 1
fruit_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0
fruits_eaten = 0

def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

def show_level(color, font, size):
    level_font = pygame.font.SysFont(font, size)
    level_surface = level_font.render('Level : ' + str(level), True, color)
    game_window.blit(level_surface, (SCREEN_WIDTH - 150, 0))

def save_game():
    cur.execute("INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s);",
                (user_id, score, level))
    conn.commit()
    print(f"Progress saved: Score = {score}, Level = {level}")

def game_over():
    save_game()
    cur.close()
    conn.close()

    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# ========== GAME LOOP ========== #
while True:
    for event in pygame.event.get():
        if event.type == FOOD_DIS:
            fruit_position = generate_fruit_position()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            elif event.key == pygame.K_p:
                print("Paused. Saving game...")
                save_game()
                paused = True
                pause_font = pygame.font.SysFont('times new roman', 30)
                pause_surface = pause_font.render('Game Paused. Press any key...', True, white)
                game_window.blit(pause_surface, (50, SCREEN_HEIGHT // 2))
                pygame.display.flip()
                while paused:
                    for e in pygame.event.get():
                        if e.type == pygame.KEYDOWN:
                            paused = False

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

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
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, (127 * fruit_weight, 0, 0, 255),
                     pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    if snake_position[0] < 0 or snake_position[0] > SCREEN_WIDTH - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > SCREEN_HEIGHT - 10:
        game_over()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(blue, 'times new roman', 35)
    show_level(blue, 'times new roman', 35)

    pygame.display.update()
    fps.tick(snake_speed)
