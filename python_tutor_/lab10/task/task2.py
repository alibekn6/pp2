import pygame
import time
import random
import psycopg2
from psycopg2 import sql
import json
import os


# Database setup (PostgreSQL with psycopg2)
def get_db_connection():
    return psycopg2.connect(
        host='localhost',
        database='suppliers',
        user='postgres',
        password='post667'
    )

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username VARCHAR(50) PRIMARY KEY,
            current_level INTEGER,
            score INTEGER,
            snake_body TEXT,
            direction VARCHAR(10),
            fruit_position TEXT,
            fruits_eaten INTEGER,
            snake_speed INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Game configuration
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BLOCK_SIZE = 10

# Define colors
colors = {
    'black': pygame.Color(0, 0, 0),
    'white': pygame.Color(255, 255, 255),
    'red': pygame.Color(255, 0, 0),
    'green': pygame.Color(0, 255, 0),
    'blue': pygame.Color(0, 0, 255)
}

# Level configurations
levels = {
    1: {
        'walls': [],
        'speed': 10,
        'fruit_weight': 1
    },
    2: {
        'walls': [[x, y] for x in range(0, SCREEN_WIDTH, BLOCK_SIZE) 
                for y in [0, SCREEN_HEIGHT-BLOCK_SIZE]] +
               [[x, y] for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE) 
                for x in [0, SCREEN_WIDTH-BLOCK_SIZE]],
        'speed': 15,
        'fruit_weight': 2
    },
    3: {
        'walls': [[x, y] for x in range(100, 300, BLOCK_SIZE) 
                for y in [100, 200]] +
               [[x, y] for y in range(100, 200, BLOCK_SIZE) 
                for x in [100, 300-BLOCK_SIZE]],
        'speed': 20,
        'fruit_weight': 3
    }
}

def get_username():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font(None, 32)
    input_box = pygame.Rect(100, 150, 200, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    text = ''
    active = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return text
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        screen.fill(colors['white'])
        txt_surface = font.render(text, True, color)
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)
        
        # Add instruction text
        instruction = font.render('Enter your username:', True, colors['black'])
        screen.blit(instruction, (100, 120))
        
        pygame.display.flip()

def save_game_state(username, level, score, snake_body, direction, fruit_pos, fruits_eaten, speed):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        sql.SQL('''
            INSERT INTO users (username, current_level, score, snake_body, direction, fruit_position, fruits_eaten, snake_speed)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (username) 
            DO UPDATE SET 
                current_level = EXCLUDED.current_level,
                score = EXCLUDED.score,
                snake_body = EXCLUDED.snake_body,
                direction = EXCLUDED.direction,
                fruit_position = EXCLUDED.fruit_position,
                fruits_eaten = EXCLUDED.fruits_eaten,
                snake_speed = EXCLUDED.snake_speed
        '''),
        (
            username,
            level,
            score,
            json.dumps(snake_body),
            direction,
            json.dumps(fruit_pos),
            fruits_eaten,
            speed
        )
    )
    conn.commit()
    conn.close()

def load_game_state(username):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        sql.SQL('SELECT * FROM users WHERE username = %s'),
        (username,)
    )
    
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return {
            'level': row[1],
            'score': row[2],
            'snake_body': json.loads(row[3]),
            'direction': row[4],
            'fruit_position': json.loads(row[5]),
            'fruits_eaten': row[6],
            'speed': row[7]
        }
    return None

def game_loop(username):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(f'Snake Game - Player: {username}')

    # Load or initialize game state
    saved_state = load_game_state(username)
    if saved_state:
        snake_body = saved_state['snake_body']
        direction = saved_state['direction']
        fruit_position = saved_state['fruit_position']
        fruits_eaten = saved_state['fruits_eaten']
        level = saved_state['level']
        score = saved_state['score']
        snake_speed = saved_state['speed']
    else:
        snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
        direction = 'RIGHT'
        fruit_position = [random.randrange(1, (SCREEN_WIDTH//BLOCK_SIZE)) * BLOCK_SIZE, 
                          random.randrange(1, (SCREEN_HEIGHT//BLOCK_SIZE)) * BLOCK_SIZE]
        fruits_eaten = 0
        level = 1
        score = 0
        snake_speed = levels[1]['speed']

    clock = pygame.time.Clock()
    change_to = direction
    fruit_spawn = True
    paused = False
    current_level_config = levels[level]

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_game_state(
                    username,
                    level,
                    score,
                    snake_body,
                    direction,
                    fruit_position,
                    fruits_eaten,
                    snake_speed
                )
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Pause and save
                    paused = not paused
                    if paused:
                        save_game_state(
                            username,
                            level,
                            score,
                            snake_body,
                            direction,
                            fruit_position,
                            fruits_eaten,
                            snake_speed
                        )
                keys = {
                    pygame.K_UP: 'UP',
                    pygame.K_DOWN: 'DOWN',
                    pygame.K_LEFT: 'LEFT',
                    pygame.K_RIGHT: 'RIGHT'
                }
                if event.key in keys and not paused:
                    change_to = keys[event.key]

        if paused:
            # Show pause message
            font = pygame.font.SysFont('arial', 30)
            pause_text = font.render('PAUSED - Press P to continue', True, colors['white'])
            screen.blit(pause_text, (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2))
            pygame.display.update()
            continue

        # Direction validation
        if change_to == 'UP' and direction != 'DOWN':
            direction = change_to
        if change_to == 'DOWN' and direction != 'UP':
            direction = change_to
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = change_to
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = change_to

        # Move snake
        head = snake_body[0].copy()
        if direction == 'UP':
            head[1] -= BLOCK_SIZE
        if direction == 'DOWN':
            head[1] += BLOCK_SIZE
        if direction == 'LEFT':
            head[0] -= BLOCK_SIZE
        if direction == 'RIGHT':
            head[0] += BLOCK_SIZE

        # Check collisions
        if (head[0] < 0 or head[0] >= SCREEN_WIDTH or
            head[1] < 0 or head[1] >= SCREEN_HEIGHT or
            head in snake_body[1:] or
            head in current_level_config['walls']):
            save_game_state(username, 1, 0, [[100,50],[90,50],[80,50],[70,50]], 
                          'RIGHT', [200, 200], 0, 10)
            game_over(score)
            return

        # Check fruit collision
        snake_body.insert(0, head)
        if head == fruit_position:
            score += 10 * level * current_level_config['fruit_weight']
            fruits_eaten += 1
            fruit_spawn = False
        else:
            snake_body.pop()

        # Level progression
        if fruits_eaten % 3 == 0 and not fruit_spawn and level < len(levels):
            level += 1
            current_level_config = levels[level]
            snake_speed = current_level_config['speed']
            fruit_spawn = True

        # Generate new fruit
        if not fruit_spawn:
            fruit_position = [random.randrange(1, (SCREEN_WIDTH//BLOCK_SIZE)) * BLOCK_SIZE,
                             random.randrange(1, (SCREEN_HEIGHT//BLOCK_SIZE)) * BLOCK_SIZE]
            while fruit_position in snake_body or fruit_position in current_level_config['walls']:
                fruit_position = [random.randrange(1, (SCREEN_WIDTH//BLOCK_SIZE)) * BLOCK_SIZE,
                                  random.randrange(1, (SCREEN_HEIGHT//BLOCK_SIZE)) * BLOCK_SIZE]
            fruit_spawn = True

        # Drawing
        screen.fill(colors['black'])
        
        # Draw walls
        for wall in current_level_config['walls']:
            pygame.draw.rect(screen, colors['white'], 
                            pygame.Rect(wall[0], wall[1], BLOCK_SIZE, BLOCK_SIZE))
        
        # Draw snake
        for segment in snake_body:
            pygame.draw.rect(screen, colors['green'], 
                            pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))
        
        # Draw fruit
        pygame.draw.rect(screen, colors['red'], 
                        pygame.Rect(fruit_position[0], fruit_position[1], BLOCK_SIZE, BLOCK_SIZE))

        # Draw UI
        font = pygame.font.SysFont('arial', 20)
        score_text = font.render(f'Score: {score}', True, colors['white'])
        level_text = font.render(f'Level: {level}', True, colors['white'])
        username_text = font.render(f'Player: {username}', True, colors['white'])
        pause_text = font.render('P: Pause', True, colors['white'])
        
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (SCREEN_WIDTH-100, 10))
        screen.blit(username_text, (10, SCREEN_HEIGHT-30))
        screen.blit(pause_text, (SCREEN_WIDTH-80, SCREEN_HEIGHT-30))

        pygame.display.update()
        clock.tick(snake_speed)

def game_over(score):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.SysFont('arial', 30)
    text = font.render(f'Game Over! Score: {score}', True, colors['red'])
    screen.blit(text, (SCREEN_WIDTH//2-100, SCREEN_HEIGHT//2))
    pygame.display.update()
    time.sleep(2)
    pygame.quit()

if __name__ == '__main__':
    # Initialize database
    init_db()
    
    # Get username and start game
    username = get_username()
    game_loop(username)