import pygame
import os
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
#KEYBOARD_KEYS = [["`", "1", "q", "a", "z"], ["2", "w", "s", "x"], ["3", "e", "d", "c"], ["4", "r", "f", "v", "5", "t", "g", "b"], ["6", "y", "h", "n", "7", "u", "j", "m"], ["8", "i", "k", "comma"], ["9", "o", "l", "period"], ["0", "p", "semicolon", "forward slash", "minus sign", "left bracket", "quote", "equals sign", "right bracket", "backslash"]]
KEYBOARD = [["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "="], ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]", "\\"], ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'"], ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]
DEFAULT_NOTE_SPEED = 5
DEFAULT_NOTE_SPACING = 100
RESULTS_POS = (WINDOW_WIDTH / 4, WINDOW_HEIGHT / 4)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GAMEPLAY_BACKGROUND = (148, 214, 247)
GRAY = (209, 209, 209)

# Hitboxes
LEFT_HAND_NOTE = []
RIGHT_HAND_NOTE = []
for i in range(4):
    LEFT_HAND_NOTE.append(pygame.Rect(10 + ((NOTE_SIZE + NOTE_OFFSET) * i), KEY_Y_POS, NOTE_SIZE, NOTE_SIZE))
    RIGHT_HAND_NOTE.append(pygame.Rect(WINDOW_WIDTH - NOTE_SIZE - 10 - ((NOTE_SIZE + NOTE_OFFSET) * i), KEY_Y_POS, NOTE_SIZE, NOTE_SIZE))

# Assets
DIFFICULTY_STARS = pygame.transform.scale(pygame.image.load('./Assets/star.png'), (30, 30))
NUMBER_ROW_KEY = pygame.transform.scale(pygame.image.load("./Assets/Number_Row_Key.png"), (NOTE_SIZE, NOTE_SIZE))
TOP_ROW_KEY = pygame.transform.scale(pygame.image.load("./Assets/Top_Row_Key.png"), (NOTE_SIZE, NOTE_SIZE))
MIDDLE_ROW_KEY = pygame.transform.scale(pygame.image.load("./Assets/Middle_Row_Key.png"), (NOTE_SIZE, NOTE_SIZE))
BOTTOM_ROW_KEY = pygame.transform.scale(pygame.image.load("./Assets/Bottom_Row_Key.png"), (NOTE_SIZE, NOTE_SIZE))
INDICATOR_KEY = pygame.transform.scale(pygame.image.load("./Assets/Indicator_Key.png"), (NOTE_SIZE, NOTE_SIZE))
KEY_COLORS = [NUMBER_ROW_KEY, TOP_ROW_KEY, MIDDLE_ROW_KEY, BOTTOM_ROW_KEY, INDICATOR_KEY]

# Global Variables
notes = []

def main(selected_song):
    global window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    run = True
    clock = pygame.time.Clock()
    currentState = LOAD_STATE
    currentSong = None

    # Sets the song to the corrosponding song for the difficulty level
    for f in os.listdir("./Songs"):
        if ".mp3" in f and f[0:len(f) - 4] == selected_song:
            # set currentSong to settings in file
            file = open("./Songs/" + f[0:len(f) - 4] + ".txt", 'r')
            songSettings = file.readline().split()
            currentSong = Song(selected_song, int(songSettings[0]), int(songSettings[1]), int(songSettings[2]))
            file.close()

    if currentSong == None:
        print("An error has occurred loading the song")
        return

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
            elif not keysPressed == None and keysPressed[pygame.key.key_code("Q")]:
                run = False
                window = pygame.display.set_mode((MENU_WIDTH, WINDOW_HEIGHT))
                pygame.mixer.music.stop()
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
        window.blit(KEY_COLORS[len(KEY_COLORS) - 1], LEFT_HAND_NOTE[i])
        window.blit(KEY_COLORS[len(KEY_COLORS) - 1], RIGHT_HAND_NOTE[i])

    # Draw notes
    for note in notes:
        window.blit(KEY_COLORS[note[1].getKeyRow()], note[0])
        window.blit(NOTE_TEXT.render(note[1].getSymbol(), 1, BLACK), (note[0].x + 20, note[0].y + 20))

    # Draw UI
    window.blit(UI_TEXT.render("Score: " + currentSong.getScore(), 1, BLACK), (10, 10))
    window.blit(UI_TEXT.render("X" + currentSong.getMultiplier(), 0, (0, 0, 0)), (280, 10))
    #window.blit(UI_TEXT.render(currentSong.getDifficulty(), 0, (0, 0, 0)), (400, 10))
    for i in range(currentSong.getDifficulty()):
        window.blit(DIFFICULTY_STARS, (WINDOW_WIDTH - 40 - (35 * i), 10))

def drawResults(currentSong):
    window.fill(GAMEPLAY_BACKGROUND)
    songSummary = currentSong.getSummary()

    # Results Screen
    pygame.draw.rect(window, GRAY, (RESULTS_POS[0], RESULTS_POS[1], WINDOW_HEIGHT / 2, WINDOW_WIDTH / 2))
    window.blit(UI_TEXT.render("Score: " + currentSong.getScore(), 1, BLACK), (RESULTS_POS[0] + WINDOW_WIDTH / 8, RESULTS_POS[0] + 20))
    window.blit(UI_TEXT.render("Notes Hit: " + songSummary[0], 1, BLACK), (RESULTS_POS[0] + 20, RESULTS_POS[1] + 60))
    window.blit(UI_TEXT.render("Notes Missed: " + songSummary[1], 1, BLACK), (RESULTS_POS[0] + 20, RESULTS_POS[1] + 100))
    window.blit(UI_TEXT.render("Press 'R' to retry", 1, BLACK), (RESULTS_POS[0] + 20, RESULTS_POS[1] + 225))
    window.blit(UI_TEXT.render("Press 'Q' to quit", 1, BLACK), (RESULTS_POS[0] + 20, RESULTS_POS[1] + 265))
        
# Loads the chart and initializes the song
def loadSong(song):
    global notes
    notes = []
    file = open("./Songs/" + song.getChart(), 'r')
    print("Song settings:", file.readline()) # Skip first line
    pygame.mixer.music.stop()
    pygame.mixer.music.load("./Songs/" + song.getMP3())
    pygame.mixer.music.play()
    pygame.mixer.music.pause()
    data = file.readlines()
    for y in range(len(data)):
        for x in range(len(data[y])):
            # Left hand notes
            if data[y][x] != " " and data[y][x] != "\n" and x < 4:
                row = assignKeyRow(data, y, x)
                note = (pygame.Rect(LEFT_HAND_NOTE[x].x, y * song.getChartSpacing() + KEY_Y_POS, NOTE_SIZE, NOTE_SIZE), Note(data[y][x], row))
                notes.append(note)
            # Right hand notes
            elif data[y][x] != " " and data[y][x] != "\n":
                row = assignKeyRow(data, y, x)
                note = (pygame.Rect(RIGHT_HAND_NOTE[3 - x].x, y * song.getChartSpacing() + KEY_Y_POS, NOTE_SIZE, NOTE_SIZE), Note(data[y][x], row))
                notes.append(note)
    pygame.time.wait(200)
    pygame.mixer.music.unpause()

def assignKeyRow(data, y, x):
    for i in range(len(KEYBOARD)):
        if data[y][x] in KEYBOARD[i]:
            return i
    return len(KEY_COLORS) - 1

if __name__ == "__main__":
    main()
