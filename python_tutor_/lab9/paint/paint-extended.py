import pygame
import sys
import math
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
current_shape = "freehand"  # Default drawing mode
start_pos = None  # For shape drawing
shapes = []  # To store all drawn shapes
freehand_lines = []  # To store temporary freehand lines

# Button rectangles
clear_button_rect = pygame.Rect(5, 5, 100, 50)
erase_button_rect = pygame.Rect(120, 5, 100, 50)
drawing_area_rect = pygame.Rect(0, 60, 700, 640) 

# Shape buttons
shape_buttons = [
    {"name": "freehand", "rect": pygame.Rect(230, 5, 80, 40), "text": "Free"},
    {"name": "square", "rect": pygame.Rect(320, 5, 80, 40), "text": "Square"},
    {"name": "right_triangle", "rect": pygame.Rect(410, 5, 80, 40), "text": "R-Tri"},
    {"name": "equilateral_triangle", "rect": pygame.Rect(500, 5, 80, 40), "text": "E-Tri"},
    {"name": "rhombus", "rect": pygame.Rect(590, 5, 80, 40), "text": "Rhombus"}
]

color_palette = [
    {"color": RED, "rect": pygame.Rect(230, 50, 30, 30)},
    {"color": GREEN, "rect": pygame.Rect(270, 50, 30, 30)},
    {"color": BLUE, "rect": pygame.Rect(310, 50, 30, 30)},
    {"color": YELLOW, "rect": pygame.Rect(350, 50, 30, 30)},
    {"color": PURPLE, "rect": pygame.Rect(390, 50, 30, 30)},
    {"color": ORANGE, "rect": pygame.Rect(430, 50, 30, 30)},
    {"color": BLACK, "rect": pygame.Rect(470, 50, 30, 30)},
    {"color": PINK, "rect": pygame.Rect(510, 50, 30, 30)},
    {"color": CYAN, "rect": pygame.Rect(550, 50, 30, 30)}
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

def draw_shape_buttons():
    font = pygame.font.Font(None, 24)
    for button in shape_buttons:
        button_color = RED if button["name"] == current_shape else BLUE
        pygame.draw.rect(DISPLAYSURF, button_color, button["rect"], border_radius=5)
        text_surface = font.render(button["text"], True, WHITE)
        text_rect = text_surface.get_rect(center=button["rect"].center)
        DISPLAYSURF.blit(text_surface, text_rect)

def process_drawing(event):
    global drawing, last_pos, start_pos, shapes, freehand_lines
    
    if event.type == MOUSEBUTTONDOWN:
        if drawing_area_rect.collidepoint(event.pos):
            if current_shape == "freehand":
                drawing = True
                last_pos = event.pos
                # Start a new line segment
                freehand_lines.append({"points": [event.pos], "color": CURRENT_COLOR, "size": CURRENT_PEN_SIZE})
            else:
                start_pos = event.pos
    
    elif event.type == MOUSEBUTTONUP:
        if current_shape == "freehand":
            drawing = False
            # Save the completed freehand drawing to shapes
            if freehand_lines and freehand_lines[-1]["points"]:
                shapes.append(("freehand", freehand_lines[-1]["points"], freehand_lines[-1]["color"], freehand_lines[-1]["size"]))
                freehand_lines = []
        elif start_pos is not None and current_shape != "freehand":
            end_pos = event.pos
            if drawing_area_rect.collidepoint(end_pos):
                if current_shape == "square":
                    size = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    # Adjust size based on mouse position direction
                    if end_pos[0] < start_pos[0]:
                        x = start_pos[0] - size
                    else:
                        x = start_pos[0]
                    if end_pos[1] < start_pos[1]:
                        y = start_pos[1] - size
                    else:
                        y = start_pos[1]
                    shapes.append(("rect", pygame.Rect(x, y, size, size), CURRENT_COLOR))
                
                elif current_shape == "right_triangle":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    shapes.append(("polygon", [(x1, y1), (x2, y1), (x1, y2)], CURRENT_COLOR))
                
                elif current_shape == "equilateral_triangle":
                    x, y = start_pos
                    size = abs(end_pos[0] - x)
                    height = int(size * math.sqrt(3) / 2)
                    if end_pos[0] < x:
                        size = -size
                    if end_pos[1] < y:
                        height = -height
                    shapes.append(("polygon", [(x, y), (x + size, y), (x + size//2, y - height)], CURRENT_COLOR))
                
                elif current_shape == "rhombus":
                    x, y = start_pos
                    dx = abs(end_pos[0] - x)
                    dy = abs(end_pos[1] - y)
                    # Adjust direction based on mouse position
                    if end_pos[0] < x:
                        dx = -dx
                    if end_pos[1] < y:
                        dy = -dy
                    shapes.append(("polygon", [(x, y - dy//2), (x + dx//2, y), 
                                             (x, y + dy//2), (x - dx//2, y)], CURRENT_COLOR))
            
            start_pos = None
    
    elif event.type == MOUSEMOTION:
        if drawing and current_shape == "freehand" and drawing_area_rect.collidepoint(event.pos):
            current_pos = event.pos
            if last_pos:
                # Add point to current freehand line
                if freehand_lines:
                    freehand_lines[-1]["points"].append(current_pos)
            last_pos = current_pos

def draw_shapes():
    # Draw permanent shapes
    for shape in shapes:
        if shape[0] == "freehand":
            points = shape[1]
            if len(points) > 1:
                pygame.draw.lines(DISPLAYSURF, shape[2], False, points, shape[3])
        elif shape[0] == "rect":
            pygame.draw.rect(DISPLAYSURF, shape[2], shape[1])
            pygame.draw.rect(DISPLAYSURF, BLACK, shape[1], 1)  # Add border
        elif shape[0] == "polygon":
            pygame.draw.polygon(DISPLAYSURF, shape[2], shape[1])
            pygame.draw.polygon(DISPLAYSURF, BLACK, shape[1], 1)  # Add border
    
    # Draw current freehand line (in progress)
    if freehand_lines and freehand_lines[-1]["points"] and len(freehand_lines[-1]["points"]) > 1:
        pygame.draw.lines(DISPLAYSURF, freehand_lines[-1]["color"], False, 
                         freehand_lines[-1]["points"], freehand_lines[-1]["size"])

# Main game loop
while True:
    # Clear the drawing area (but preserve the toolbar area)
    pygame.draw.rect(DISPLAYSURF, WHITE, drawing_area_rect)
    
    # Draw all stored shapes
    draw_shapes()
    
    # Draw UI elements
    clear_button()
    erase_button()
    draw_color_palette()
    draw_shape_buttons()
    
    # Display current mode
    font = pygame.font.Font(None, 30)
    mode_text = font.render(f"Mode: {current_shape}", True, BLACK)
    DISPLAYSURF.blit(mode_text, (10, 60))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == MOUSEBUTTONDOWN:
            if clear_button_rect.collidepoint(event.pos):
                # Clear the drawing area only
                shapes = []
                freehand_lines = []
            
            elif erase_button_rect.collidepoint(event.pos):
                erase_mode = not erase_mode
                if erase_mode:
                    CURRENT_COLOR = WHITE
                    CURRENT_PEN_SIZE = 20
                    current_shape = "freehand"
                else:
                    CURRENT_COLOR = BLUE
                    CURRENT_PEN_SIZE = 5
            
            else:
                # Check color palette clicks
                for item in color_palette:
                    if item['rect'].collidepoint(event.pos):
                        CURRENT_COLOR = item['color']
                        erase_mode = False
                        CURRENT_PEN_SIZE = 5
                
                # Check shape button clicks
                for button in shape_buttons:
                    if button['rect'].collidepoint(event.pos):
                        current_shape = button['name']
                        erase_mode = False
                        if current_shape == "freehand":
                            CURRENT_PEN_SIZE = 5
        
        process_drawing(event)
    
    pygame.display.update()
    clock.tick(FPS)