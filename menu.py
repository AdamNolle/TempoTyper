import pygame
import sys
import os

# Initialize Pygame
pygame.init()
pygame.display.set_caption("Tempo Typer")

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)  # Color for unselected buttons

# Load background image
background = pygame.image.load('./Assets/notebook.png')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Font
FONT = pygame.font.SysFont(None, 48)

# Constants
BUTTON_WIDTH = SCREEN_WIDTH - 300
BUTTON_HEIGHT = 50
BUTTON_OFFSET = 70
TOP_MARGIN = 50
LEFT_MARGIN = 150

# Get list of songs
songs = []
for songName in os.listdir("./Songs"):
    if ".mp3" in songName and songName[0:len(songName) - 4] not in songs:
        # Tuple contents: (Button Rect, Song name)
        songTuple = (pygame.Rect(LEFT_MARGIN, TOP_MARGIN + (BUTTON_OFFSET * len(songs)), BUTTON_WIDTH, BUTTON_HEIGHT), songName[0:len(songName) - 4])
        songs.append(songTuple)

# Button definitions
button_start = pygame.Rect(250, 500, 200, 50)
button_quit = pygame.Rect(460, 500, 200, 50)


# Track selected difficulty
selected_song = None

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_quit.collidepoint(event.pos):
                running = False
            elif button_start.collidepoint(event.pos):
                # Start the game with selected song
                if not selected_song == None:
                    print(f"Starting game with chosen song: {selected_song}")
                    import main
                    main.main(selected_song)
                    selected_song = None
            else:
                for song in songs:
                    if song[0].collidepoint(event.pos):
                        selected_song = song[1]

    # Draw background
    screen.blit(background, (0, 0))

    # Draw buttons and text
    for song in songs:
        pygame.draw.rect(screen, WHITE if selected_song == song[1] else GREY, song[0])
        song_text = FONT.render(song[1], True, BLACK)
        screen.blit(song_text, (song[0].x + 10, song[0].y + 10))

    pygame.draw.rect(screen, WHITE, button_start)
    pygame.draw.rect(screen, WHITE, button_quit)
    start_text = FONT.render('Start', True, BLACK)
    quit_text = FONT.render('Quit', True, BLACK)
    screen.blit(start_text, (button_start.x + 50, button_start.y + 10))
    screen.blit(quit_text, (button_quit.x + 50, button_quit.y + 10))

    # Update the display
    pygame.display.flip()

pygame.quit()
