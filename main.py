import pygame

pygame.font.init()
pygame.display.set_caption("Tempo Typer")

# Window settings
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 600
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
FPS = 60
GAMEPLAY_BACKGROUND = (5, 183, 237)

# Program constants
MAIN_MENU_STATE, SONG_SELECT_STATE, GAMEPLAY_STATE = 0, 1, 2
NOTE_TEXT = pygame.font.SysFont("ariel", 20)
NOTE_SIZE = 50
NOTE_OFFSET = 20

# Hitboxes
LEFT_HAND_NOTE = []
RIGHT_HAND_NOTE = []
for i in range(4):
    LEFT_HAND_NOTE.append((10 + ((NOTE_SIZE + NOTE_OFFSET) * i), 50, NOTE_SIZE, NOTE_SIZE))
    RIGHT_HAND_NOTE.append((WINDOW_WIDTH - NOTE_SIZE - 10 - ((NOTE_SIZE + NOTE_OFFSET) * i), 50, NOTE_SIZE, NOTE_SIZE))

def main():
    run = True
    clock = pygame.time.Clock()
    currentState = GAMEPLAY_STATE # Change to MAIN_MENU_STATE once implemented

    # Variables
    keysPressed = []

    # Repeats until user exits program
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                keysPressed = pygame.key.get_pressed()

        if currentState == MAIN_MENU_STATE:
            mainMenu()
            drawMainMenu()
        elif currentState == SONG_SELECT_STATE:
            songSelect()
            drawSongSelect()
        elif currentState == GAMEPLAY_STATE:
            gameplay(keysPressed)
            drawGameplay()
        else:
            pygame.error("Error: Entered invalid state")
        pygame.display.update()

    pygame.quit()

# Handles main menu logic
def mainMenu():
    pass

# Draws main menu assets
def drawMainMenu():
    pass

# Handles song selection logic
def songSelect():
    pass

# Draws song selection assets
def drawSongSelect():
    pass

# Handles main gameplay logic
def gameplay(keysPressed):
    pass

# Draws gameplay assets
def drawGameplay():
    WINDOW.fill(GAMEPLAY_BACKGROUND)
    for i in range(4):
        pygame.draw.rect(WINDOW, (191, 197, 199), LEFT_HAND_NOTE[i])
        pygame.draw.rect(WINDOW, (191, 197, 199), RIGHT_HAND_NOTE[i])

if __name__ == "__main__":
    main()