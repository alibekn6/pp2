import pygame
from pygame.locals import *

pygame.init()

WHITE =     (255, 255, 255)
BLUE =      (  0,   0, 255)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)
FPS = 60

DISPLAYSURF = pygame.display.set_mode((700,700))
pygame.display.set_caption("Xolst")
DISPLAYSURF.fill(WHITE)

clock = pygame.time.Clock()

drawing = False
last_pos = None
CURRENT_COLOR = BLUE  # Default drawing color
CURRENT_PEN_SIZE = 5 # default size of pen

clear_button_rect = pygame.Rect(5, 5, 100, 50)
erase_button_rect = pygame.Rect(120, 5, 100, 50)


def clear_button():
    font = pygame.font.Font(None, 40)  

    button_color = BLUE
    text_surface = font.render("clear", True, WHITE)
    text_rect = text_surface.get_rect(center=clear_button_rect.center)


    pygame.draw.rect(DISPLAYSURF, button_color, clear_button_rect, border_radius=10)
    DISPLAYSURF.blit(text_surface, text_rect)

def erase_button():
    font = pygame.font.Font(None, 40)  

    button_color = RED if CURRENT_COLOR == WHITE else BLUE

    text_surface = font.render("erase", True, WHITE)
    text_rect = text_surface.get_rect(center=erase_button_rect.center)


    pygame.draw.rect(DISPLAYSURF, button_color, erase_button_rect, border_radius=10)
    DISPLAYSURF.blit(text_surface, text_rect)




def draw(event):

    global drawing, last_pos
    if event.type == MOUSEBUTTONDOWN:
        if not (clear_button_rect.collidepoint(event.pos) or erase_button_rect.collidepoint(event.pos)):
            drawing = True
            last_pos = event.pos
    
    if event.type == MOUSEBUTTONUP:
        drawing = False
        last_pos = None

    if event.type == MOUSEMOTION and drawing:
        current_pos = event.pos
        if last_pos:
            pygame.draw.line(DISPLAYSURF, CURRENT_COLOR, last_pos, current_pos, CURRENT_PEN_SIZE)
        last_pos = current_pos




while True:
    
    clear_button()
    erase_button()

    for event in pygame.event.get():
        draw(event)

        if event.type == QUIT:
            pygame.quit()
        
        if event.type == MOUSEBUTTONDOWN:
            if clear_button_rect.collidepoint(event.pos):
                print("BUTTON CLIKEDD!!!!")
                DISPLAYSURF.fill(WHITE)
            
            if erase_button_rect.collidepoint(event.pos):
                if CURRENT_COLOR == BLUE:
                    CURRENT_COLOR = WHITE
                    CURRENT_PEN_SIZE = 20
                    print("Erase mode on")
                else:
                    CURRENT_COLOR = BLUE
                    CURRENT_PEN_SIZE = 5
                    print("DRAW MODE ON")
                


    pygame.display.update()
    clock.tick(FPS)