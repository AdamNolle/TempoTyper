import pygame
from note import Note
from song import Song

pygame.font.init()
pygame.mixer.init()
pygame.display.set_caption("Tempo Typer")

# Window settings
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 600
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
FPS = 60
NOTE_TEXT = pygame.font.SysFont("ariel", 20)
UI_TEXT = pygame.font.SysFont("ariel", 40)

# Program constants
MAIN_MENU_STATE, SONG_SELECT_STATE, GAMEPLAY_STATE = 0, 1, 2
NOTE_SIZE = 50
NOTE_OFFSET = 20
NOTE_DISTANCE = 100
KEY_Y_POS = 50
#KEYBOARD_KEYS = [["1", "q", "a", "z"], ["2", "w", "s", "x"], ["3", "e", "d", "c"], ["4", "r", "f", "v", "5", "t", "g", "b"], ["6", "y", "h", "n", "7", "u", "j", "m"], ["8", "i", "k", "comma"], ["9", "o", "l", "period"], ["0", "p", "semicolon", "forward slash", "minus sign", "left bracket", "quote", "equals sign", "right bracket", "backslash"]]
SONG_LIST = [Song("TestSong", 5, "Easy"), Song("EasySong", 5, "Easy"), Song("MediumSong", 5, "Medium"), Song("HardSong", 5, "Hard")]

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
KEY_COLOR = (191, 197, 199)
GAMEPLAY_BACKGROUND = (5, 183, 237)

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
    currentSong = SONG_LIST[0]

    # Variables
    keysPressed = None

    # Repeats until user exits program
    while run:
        clock.tick(FPS)
        keysPressed = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                keysPressed = pygame.key.get_pressed()

        if currentState == MAIN_MENU_STATE:
            mainMenu()
            drawMainMenu()
        elif currentState == SONG_SELECT_STATE:
            currentState = songSelect(currentSong)
            drawSongSelect()
        elif currentState == GAMEPLAY_STATE:
            gameplay(keysPressed, currentSong)
            drawGameplay(currentSong)
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
def songSelect(currentSong):
    # Show list of songs

    # Load song once selected
    currentSong.reset()
    loadSong(currentSong)  # Test song
    return GAMEPLAY_STATE


# Draws song selection assets
def drawSongSelect():
    pass

# Handles main gameplay logic
def gameplay(keysPressed, currentSong):
    global notes

    # Check if keys have been pressed
    if not keysPressed == None:
        for index in range(len(LEFT_HAND_NOTE)):
            for note in notes:
                if LEFT_HAND_NOTE[index].colliderect(note[0]) or RIGHT_HAND_NOTE[index].colliderect(note[0]):
                    if keysPressed[pygame.key.key_code(note[1].getSymbol())]:
                        notes.remove(note)
                        currentSong.noteHit()

    # Move notes in the chart
    for note in notes:
        if note[0].y <= 0:
            notes.remove(note)
            currentSong.noteMiss()
        else:
            note[0].y -= currentSong.getChartSpeed()

# Draws gameplay assets
def drawGameplay(currentSong):
    global notes
    WINDOW.fill(GAMEPLAY_BACKGROUND)
    # Draw keys
    for i in range(4):
        pygame.draw.rect(WINDOW, KEY_COLOR, LEFT_HAND_NOTE[i])
        pygame.draw.rect(WINDOW, KEY_COLOR, RIGHT_HAND_NOTE[i])

    # Draw notes
    for note in notes:
        pygame.draw.rect(WINDOW, WHITE, note[0])
        WINDOW.blit(NOTE_TEXT.render(note[1].getSymbol(), 1, BLACK), (note[0].x + 20, note[0].y + 20))

    # Draw UI
    WINDOW.blit(UI_TEXT.render("Score: " + currentSong.getScore(), 1, BLACK), (10, 10))
    WINDOW.blit(UI_TEXT.render("Multiplier: " + currentSong.getMultiplier(), 0, (0, 0, 0)), (200, 10))
    WINDOW.blit(UI_TEXT.render(currentSong.getDifficulty(), 0, (0, 0, 0)), (400, 10))
        
# Loads the chart and initializes the song
def loadSong(song):
    global notes
    notes = []
    file = open("./Songs/" + song.getChart(), 'r')
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
    #pygame.mixer.music.load("./Songs/" + song.getMP3())
    #pygame.mixer.music.play()

if __name__ == "__main__":
    main()