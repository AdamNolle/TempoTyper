import pygame
from note import Note

pygame.font.init()
pygame.mixer.init()
pygame.display.set_caption("Tempo Typer")

# Window settings
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 600
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
FPS = 60
GAMEPLAY_BACKGROUND = (5, 183, 237)
TEXT_FONT = pygame.font.SysFont("ariel", 20)

# Program constants
MAIN_MENU_STATE, SONG_SELECT_STATE, GAMEPLAY_STATE = 0, 1, 2
NOTE_TEXT = pygame.font.SysFont("ariel", 20)
NOTE_SIZE = 50
NOTE_OFFSET = 20
NOTE_SPEED = 5
NOTE_DISTANCE = 100
KEY_Y_POS = 50
KEYBOARD_KEYS = [["1", "q", "a", "z"], ["2", "w", "s", "x"], ["3", "e", "d", "c"], ["4", "r", "f", "v", "5", "t", "g", "b"], ["6", "y", "h", "n", "7", "u", "j", "m"], ["8", "i", "k", "comma"], ["9", "o", "l", "period"], ["0", "p", "semicolon", "forward slash", "minus sign", "left bracket", "quote", "equals sign", "right bracket", "backslash"]]
SONG_LIST = [("TestSong.mp3", "./Songs/TestSong.txt"), ("EasySong.mp3", "EasySong.txt"), ("MediumSong.mp3", "MediumSong.txt"), ("HardSong.mp3", "HardSong.txt")]

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
KEY_COLOR = (191, 197, 199)

# Hitboxes
LEFT_HAND_NOTE = []
RIGHT_HAND_NOTE = []
for i in range(4):
    LEFT_HAND_NOTE.append(pygame.Rect(10 + ((NOTE_SIZE + NOTE_OFFSET) * i), KEY_Y_POS, NOTE_SIZE, NOTE_SIZE))
    RIGHT_HAND_NOTE.append(pygame.Rect(WINDOW_WIDTH - NOTE_SIZE - 10 - ((NOTE_SIZE + NOTE_OFFSET) * i), KEY_Y_POS, NOTE_SIZE, NOTE_SIZE))

# Global Variables
notes = []

def main():
    run = True
    clock = pygame.time.Clock()
    currentState = SONG_SELECT_STATE # Change to MAIN_MENU_STATE once implemented

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
            currentState = songSelect()
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
    # Show list of songs

    # Load song once selected
    loadSong(SONG_LIST[0])  # Test song
    return GAMEPLAY_STATE


# Draws song selection assets
def drawSongSelect():
    pass

# Handles main gameplay logic
def gameplay(keysPressed):
    global notes
    # Check if keys have been pressed

    # Move notes in the chart
    for note in notes:
        if note[0].y <= 0:
            notes.remove(note)
        else:
            note[0].y -= NOTE_SPEED

# Draws gameplay assets
def drawGameplay():
    global notes
    WINDOW.fill(GAMEPLAY_BACKGROUND)
    # Draw keys
    for i in range(4):
        pygame.draw.rect(WINDOW, KEY_COLOR, LEFT_HAND_NOTE[i])
        pygame.draw.rect(WINDOW, KEY_COLOR, RIGHT_HAND_NOTE[i])

    # Draw notes
    for note in notes:
        pygame.draw.rect(WINDOW, WHITE, note[0])
        WINDOW.blit(TEXT_FONT.render(note[1].getSymbol(), 1, BLACK), (note[0].x + 20, note[0].y + 20))

# Loads the chart and initializes the song
def loadSong(song):
    global notes
    notes = []
    file = open(song[1], 'r')
    data = file.readlines()
    for y in range(len(data)):
        for x in range(len(data[y])):
            # Left hand notes
            if data[y][x] != " " and data[y][x] != "\n" and x < 4:
                note = (pygame.Rect(LEFT_HAND_NOTE[x].x, y * NOTE_DISTANCE + KEY_Y_POS, NOTE_SIZE, NOTE_SIZE), Note(data[y][x]))
                notes.append(note)
            # Right hand notes
            elif data[y][x] != " " and data[y][x] != "\n":
                note = (pygame.Rect(RIGHT_HAND_NOTE[3 - x].x, y * NOTE_DISTANCE + KEY_Y_POS, NOTE_SIZE, NOTE_SIZE), Note(data[y][x]))
                notes.append(note)
    #pygame.mixer.music.load(song[0])
    #pygame.mixer.music.play()

if __name__ == "__main__":
    main()