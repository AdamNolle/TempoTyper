import pygame
from note import Note
from song import Song

pygame.font.init()
pygame.mixer.init()
pygame.display.set_caption("Tempo Typer")

# Window settings
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 600
MENU_WIDTH = 800
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
FPS = 60
NOTE_TEXT = pygame.font.SysFont("ariel", 30)
UI_TEXT = pygame.font.SysFont("ariel", 40)

# Program constants
LOAD_STATE, GAMEPLAY_STATE, RESULTS_STATE = 0, 1, 2
EASY, MEDIUM, HARD = 1, 2, 3
NOTE_SIZE = 50
NOTE_OFFSET = 20
KEY_Y_POS = 50
#KEYBOARD_KEYS = [["1", "q", "a", "z"], ["2", "w", "s", "x"], ["3", "e", "d", "c"], ["4", "r", "f", "v", "5", "t", "g", "b"], ["6", "y", "h", "n", "7", "u", "j", "m"], ["8", "i", "k", "comma"], ["9", "o", "l", "period"], ["0", "p", "semicolon", "forward slash", "minus sign", "left bracket", "quote", "equals sign", "right bracket", "backslash"]]
DEFAULT_NOTE_SPEED = 5
DEFAULT_NOTE_SPACING = 100
SONG_LIST = [Song("TestSong", 8, 25, "Test"), Song("EasySong", DEFAULT_NOTE_SPEED, 25, "Easy"), Song("MediumSong", 4, 25, "Medium"), Song("HardSong", DEFAULT_NOTE_SPEED, DEFAULT_NOTE_SPACING, "Hard")]
RESULTS_POS = (WINDOW_WIDTH / 4, WINDOW_HEIGHT / 4)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
KEY_COLOR = (191, 197, 199)
GAMEPLAY_BACKGROUND = (5, 183, 237)
GRAY = (155, 155, 155)

# Hitboxes
LEFT_HAND_NOTE = []
RIGHT_HAND_NOTE = []
for i in range(4):
    LEFT_HAND_NOTE.append(pygame.Rect(10 + ((NOTE_SIZE + NOTE_OFFSET) * i), KEY_Y_POS, NOTE_SIZE, NOTE_SIZE))
    RIGHT_HAND_NOTE.append(pygame.Rect(WINDOW_WIDTH - NOTE_SIZE - 10 - ((NOTE_SIZE + NOTE_OFFSET) * i), KEY_Y_POS, NOTE_SIZE, NOTE_SIZE))

# Assets
DIFFICULTY_STARS = pygame.transform.scale(pygame.image.load('./Assets/star.png'), (50, 50))

# Global Variables
notes = []

def main(selected_difficulty):
    global window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    run = True
    clock = pygame.time.Clock()
    currentState = LOAD_STATE
    currentSong = SONG_LIST[0]  # Test song by default

    # Sets the song to the corrosponding song for the difficulty level
    for song in SONG_LIST:
        if song.getDifficulty() == selected_difficulty:
            currentSong = song
            break

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

        if currentState == LOAD_STATE:
            currentSong.reset()
            loadSong(currentSong)
            currentState = GAMEPLAY_STATE
        elif currentState == GAMEPLAY_STATE:
            if len(notes) == 0:
                pygame.time.wait(500)
                keysPressed = None
                currentState = RESULTS_STATE
            gameplay(keysPressed, currentSong)
            drawGameplay(currentSong)
        elif currentState == RESULTS_STATE:
            drawResults(currentSong)
            if not keysPressed == None and keysPressed[pygame.key.key_code("R")]:
                currentState = LOAD_STATE
            elif not keysPressed == None:
                run = False
                window = pygame.display.set_mode((MENU_WIDTH, WINDOW_HEIGHT))
                return
        else:
            pygame.error("Error: Entered invalid state")
        pygame.display.update()

    pygame.quit()

# Handles main gameplay logic
def gameplay(keysPressed, currentSong):
    global notes

    # Check if keys have been pressed
    if not keysPressed == None:
        for index in range(len(LEFT_HAND_NOTE)):
            for note in range(0, 8):
                if note < len(notes) and (LEFT_HAND_NOTE[index].colliderect(notes[note][0]) or RIGHT_HAND_NOTE[index].colliderect(notes[note][0])):
                    if keysPressed[pygame.key.key_code(notes[note][1].getSymbol())]:
                        notes.remove(notes[note])
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
    window.fill(GAMEPLAY_BACKGROUND)
    # Draw keys
    for i in range(4):
        pygame.draw.rect(window, KEY_COLOR, LEFT_HAND_NOTE[i])
        pygame.draw.rect(window, KEY_COLOR, RIGHT_HAND_NOTE[i])

    # Draw notes
    for note in notes:
        pygame.draw.rect(window, WHITE, note[0])
        window.blit(NOTE_TEXT.render(note[1].getSymbol(), 1, BLACK), (note[0].x + 20, note[0].y + 20))

    # Draw UI
    window.blit(UI_TEXT.render("Score: " + currentSong.getScore(), 1, BLACK), (10, 10))
    window.blit(UI_TEXT.render("Multiplier: " + currentSong.getMultiplier(), 0, (0, 0, 0)), (200, 10))
    window.blit(UI_TEXT.render(currentSong.getDifficulty(), 0, (0, 0, 0)), (400, 10))

def drawResults(currentSong):
    window.fill(GAMEPLAY_BACKGROUND)
    songSummary = currentSong.getSummary()

    # Results Screen
    pygame.draw.rect(window, KEY_COLOR, (RESULTS_POS[0], RESULTS_POS[1], WINDOW_HEIGHT / 2, WINDOW_WIDTH / 2))
    window.blit(UI_TEXT.render("Score: " + currentSong.getScore(), 1, BLACK), (RESULTS_POS[0] + WINDOW_WIDTH / 8, RESULTS_POS[0] + 20))
    window.blit(UI_TEXT.render("Notes Hit: " + songSummary[0], 1, BLACK), (RESULTS_POS[0] + 20, RESULTS_POS[1] + 60))
    window.blit(UI_TEXT.render("Notes Missed: " + songSummary[1], 1, BLACK), (RESULTS_POS[0] + 20, RESULTS_POS[1] + 100))
    window.blit(UI_TEXT.render("Press 'R' to replay", 1, BLACK), (RESULTS_POS[0] + 20, RESULTS_POS[1] + 250))
        
# Loads the chart and initializes the song
def loadSong(song):
    global notes
    notes = []
    file = open("./Songs/" + song.getChart(), 'r')  # Change the first part of the path if there is an error
    data = file.readlines()
    for y in range(len(data)):
        for x in range(len(data[y])):
            # Left hand notes
            if data[y][x] != " " and data[y][x] != "\n" and x < 4:
                note = (pygame.Rect(LEFT_HAND_NOTE[x].x, y * song.getChartSpacing() + KEY_Y_POS, NOTE_SIZE, NOTE_SIZE), Note(data[y][x]))
                notes.append(note)
            # Right hand notes
            elif data[y][x] != " " and data[y][x] != "\n":
                note = (pygame.Rect(RIGHT_HAND_NOTE[3 - x].x, y * song.getChartSpacing() + KEY_Y_POS, NOTE_SIZE, NOTE_SIZE), Note(data[y][x]))
                notes.append(note)
    pygame.mixer.stop()
    pygame.mixer.music.load("./Songs/" + song.getMP3())
    pygame.time.wait(100)
    pygame.mixer.music.play()

if __name__ == "__main__":
    main()
