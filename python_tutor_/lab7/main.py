import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
done = False
is_blue = True
colorRgb = ()
x = 30
y = 30

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        colorRgb = (255, 0, 0)
            
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 1
        if pressed[pygame.K_DOWN]: y += 1
        if pressed[pygame.K_LEFT]: x -= 1
        if pressed[pygame.K_RIGHT]: x += 1
        
        if is_blue:
            color = (0, 128, 255)            
        else: 
            color = (255, 100, 0)
        color = colorRgb
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        
        pygame.display.flip()
