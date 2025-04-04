import pygame
import sys
from pygame.locals import *

pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
PINK = (255, 192, 203)
CYAN = (0, 255, 255)
FPS = 60

# Display setup
DISPLAYSURF = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Xolst")
DISPLAYSURF.fill(WHITE)

clock = pygame.time.Clock()

# Drawing variables
drawing = False
last_pos = None
CURRENT_COLOR = BLUE  # Default drawing color
CURRENT_PEN_SIZE = 5  # Default size of pen
erase_mode = False


clear_button_rect = pygame.Rect(5, 5, 100, 50)
erase_button_rect = pygame.Rect(120, 5, 100, 50)
drawing_area_rect = pygame.Rect(0, 60, 700, 640) 

color_palette = [
    {"color": RED, "rect": pygame.Rect(230, 5, 40, 40)},
    {"color": GREEN, "rect": pygame.Rect(280, 5, 40, 40)},
    {"color": BLUE, "rect": pygame.Rect(330, 5, 40, 40)},
    {"color": YELLOW, "rect": pygame.Rect(380, 5, 40, 40)},
    {"color": PURPLE, "rect": pygame.Rect(430, 5, 40, 40)},
    {"color": ORANGE, "rect": pygame.Rect(480, 5, 40, 40)},
    {"color": BLACK, "rect": pygame.Rect(530, 5, 40, 40)},
    {"color": PINK, "rect": pygame.Rect(580, 5, 40, 40)},
    {"color": CYAN, "rect": pygame.Rect(630, 5, 40, 40)}
]


def clear_button():
    font = pygame.font.Font(None, 40)
    button_color = BLUE
    text_surface = font.render("clear", True, WHITE)
    text_rect = text_surface.get_rect(center=clear_button_rect.center)
    
    pygame.draw.rect(DISPLAYSURF, button_color, clear_button_rect, border_radius=10)
    DISPLAYSURF.blit(text_surface, text_rect)

def erase_button():
    font = pygame.font.Font(None, 40)
    button_color = RED if erase_mode else BLUE
    text_surface = font.render("erase", True, WHITE)
    text_rect = text_surface.get_rect(center=erase_button_rect.center)
    
    pygame.draw.rect(DISPLAYSURF, button_color, erase_button_rect, border_radius=10)
    DISPLAYSURF.blit(text_surface, text_rect)

def draw_color_palette():
    for item in color_palette:
        color = item["color"]
        rect = item["rect"]
        
        # Draw the color swatch
        pygame.draw.rect(DISPLAYSURF, color, rect)
        
        # Draw border (thicker for current color)
        border_width = 3 if color == CURRENT_COLOR and not erase_mode else 1
        border_color = BLACK if color != BLACK else WHITE
        pygame.draw.rect(DISPLAYSURF, border_color, rect, border_width)



def process_drawing(event):
    global drawing, last_pos
    
    if event.type == MOUSEBUTTONDOWN:
        if drawing_area_rect.collidepoint(event.pos):
            drawing = True
            last_pos = event.pos
    
    elif event.type == MOUSEBUTTONUP:
        drawing = False
        last_pos = None
    
    elif event.type == MOUSEMOTION and drawing:
        if drawing_area_rect.collidepoint(event.pos):
            current_pos = event.pos
            if last_pos:
                pygame.draw.line(DISPLAYSURF, CURRENT_COLOR, last_pos, current_pos, CURRENT_PEN_SIZE)
            last_pos = current_pos

# Main game loop
while True:
    clear_button()
    erase_button()
    draw_color_palette()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == MOUSEBUTTONDOWN:
            if clear_button_rect.collidepoint(event.pos):
                # Clear the drawing area only
                pygame.draw.rect(DISPLAYSURF, WHITE, drawing_area_rect)
            
            elif erase_button_rect.collidepoint(event.pos):
                erase_mode = not erase_mode
                if erase_mode:
                    CURRENT_COLOR = WHITE
                    CURRENT_PEN_SIZE = 20
                else:
                    CURRENT_COLOR = BLUE
                    CURRENT_PEN_SIZE = 5

            else:
                for item in color_palette:
                    if item['rect'].collidepoint(event.pos):
                        CURRENT_COLOR = item['color']
                        erase_mode = False
                        CURRENT_PEN_SIZE = 5
        

        process_drawing(event)
    
    pygame.display.update()
    clock.tick(FPS)