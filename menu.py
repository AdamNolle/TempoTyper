import pygame
import sys

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

# Button definitions
button_easy = pygame.Rect(100, 50, 200, 50)
button_medium = pygame.Rect(300, 50, 200, 50)
button_hard = pygame.Rect(500, 50, 200, 50)
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
                # Start the game with selected difficulty
                print(f"Starting game with difficulty: {selected_song}")
                import main
                main.main(selected_song)
                selected_song = None
            elif button_easy.collidepoint(event.pos):
                selected_song = 'EasySong'
            elif button_medium.collidepoint(event.pos):
                selected_song = 'MediumSong'
            elif button_hard.collidepoint(event.pos):
                selected_song = 'HardSong'

    # Draw background
    screen.blit(background, (0, 0))

    # Draw buttons
    pygame.draw.rect(screen, WHITE if selected_song == 'EasySong' else GREY, button_easy)
    pygame.draw.rect(screen, WHITE if selected_song == 'MediumSong' else GREY, button_medium)
    pygame.draw.rect(screen, WHITE if selected_song == 'HardSong' else GREY, button_hard)
    pygame.draw.rect(screen, WHITE, button_start)
    pygame.draw.rect(screen, WHITE, button_quit)

    # Draw button texts
    easy_text = FONT.render('Easy', True, BLACK)
    medium_text = FONT.render('Medium', True, BLACK)
    hard_text = FONT.render('Hard', True, BLACK)
    start_text = FONT.render('Start', True, BLACK)
    quit_text = FONT.render('Quit', True, BLACK)

    screen.blit(easy_text, (button_easy.x + 50, button_easy.y + 10))
    screen.blit(medium_text, (button_medium.x + 50, button_medium.y + 10))
    screen.blit(hard_text, (button_hard.x + 50, button_hard.y + 10))
    screen.blit(start_text, (button_start.x + 50, button_start.y + 10))
    screen.blit(quit_text, (button_quit.x + 50, button_quit.y + 10))

    # Update the display
    pygame.display.flip()

pygame.quit()
