import pygame
import os

pygame.init()
pygame.mixer.init()

# Set up display
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")


WHITE = (255, 255, 255)
SPOTIFY_GREEN = (101, 212, 110)
BLACK = (0, 0, 0)


font = pygame.font.Font(None, 36)


music_dir = "music" # folder
music_files = [f for f in os.listdir(music_dir) if f.endswith(('.mp3', '.wav', '.m4a'))]
current_track = 0
playing = False

def play_music():
    global playing
    if not playing:
        pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))
        pygame.mixer.music.play()
        playing = True

def stop_music():
    global playing
    pygame.mixer.music.pause()
    playing = False

def next_track():
    global current_track, playing
    playing = False
    current_track = (current_track + 1) % len(music_files)
    play_music()

def previous_track():
    global current_track, playing
    playing = False
    current_track = (current_track - 1) % len(music_files)
    play_music()

# Main game loop
running = True
while running:

    logo_image = pygame.image.load("spoti.png")
    logo_image = pygame.transform.scale(logo_image, (200, 200))  


    screen.fill(BLACK)

    logo_x = WIDTH // 2 - logo_image.get_width() // 2  # Center horizontally
    logo_y = HEIGHT // 4 - logo_image.get_height() // 2  # Position in the top quarter
    screen.blit(logo_image, (logo_x, logo_y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Play/Stop
                if playing:
                    stop_music()
                else:
                    play_music()
            elif event.key == pygame.K_RIGHT:  # Next track
                next_track()
            elif event.key == pygame.K_LEFT:  # Previous track
                previous_track()

    # Display current track and status
    status = "Playing" if playing else "Stopped"
    current_song = music_files[current_track].split('.')[0]
    
    status_text = font.render(f"Status: {status}", True, WHITE)
    song_text = font.render(f"Current Song: {current_song}", True, WHITE)
    controls_text = font.render("Controls: SPACE = Play/Stop, LEFT/RIGHT = Previous/Next", True, WHITE)
    song_list_dir = os.listdir(music_dir)



    # song_names = [os.path.splitext(song)[0] for song in song_list_dir]
    # song_list_string = "\n".join(song_names)
    # song_list = font.render(f"Song avaliable {song_names}", True, WHITE)

    screen.blit(status_text, (20, 20))
    screen.blit(song_text, (20, 60))
    screen.blit(controls_text, (20, HEIGHT - 40))
    song_list = [os.path.splitext(song)[0] for song in song_list_dir]  # Optional: remove file extensions

    # In your main game loop where you're drawing to the screen:
    line_height = 30  # Adjust based on your font size
    start_y = 500   # Starting Y position for the first line
    start_x = 20     # X position for all lines

    # Loop through each song and render it on a new line
    for i, song in enumerate(song_list):
        song_text = font.render(song, True, WHITE)
        screen.blit(song_text, (start_x, start_y + i * line_height))

    

    
    pygame.display.flip()

pygame.quit()
