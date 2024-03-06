import pygame
import random

pygame.font.init()

WIDTH, HEIGHT = 700, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
BG = (5, 183, 237)
FPS = 60

TEXT_FONT = pygame.font.SysFont("ariel", 20)
UI_FONT = pygame.font.SysFont("ariel", 40)
LEFT_PINKY_NOTE = pygame.Rect(10, 50, 50, 50)
LEFT_RING_NOTE = pygame.Rect(80, 50, 50, 50)
LEFT_MIDDLE_NOTE = pygame.Rect(150, 50, 50, 50)
LEFT_INDEX_NOTE = pygame.Rect(220, 50, 50, 50)
RIGHT_INDEX_NOTE = pygame.Rect(430, 50, 50, 50)
RIGHT_MIDDLE_NOTE = pygame.Rect(500, 50, 50, 50)
RIGHT_RING_NOTE = pygame.Rect(570, 50, 50, 50)
RIGHT_PINKY_NOTE = pygame.Rect(640, 50, 50, 50)
DIFFICULTY = ["Easy", "Normal", "Hard", "Impossible"]
MULTIPLIER_MAX = 5
MULTIPLIER_MIN = 1

pygame.display.set_caption("This is a prototype")

score = 0
multiplier = MULTIPLIER_MIN
notesHit = 0

def main():
    global BG
    run = True
    clock = pygame.time.Clock()

    notes = []
    note_speed = 5
    difficulty = DIFFICULTY[0]  # Change the number to change the difficulty

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                keys_pressed = pygame.key.get_pressed()
                process_click(keys_pressed, notes)
        move_notes(notes, note_speed, difficulty)
        draw_window(notes, difficulty)
    
    pygame.quit()

def draw_window(notes, difficulty): # Graphic design is my passion
    WINDOW.fill(BG)

    # Note indicators
    pygame.draw.rect(WINDOW, (191, 197, 199), LEFT_PINKY_NOTE) # Left pinky
    pygame.draw.rect(WINDOW, (191, 197, 199), LEFT_RING_NOTE) # Left ring
    pygame.draw.rect(WINDOW, (191, 197, 199), LEFT_MIDDLE_NOTE) # Left middle
    pygame.draw.rect(WINDOW, (191, 197, 199), LEFT_INDEX_NOTE) # Left index
    pygame.draw.rect(WINDOW, (191, 197, 199), RIGHT_INDEX_NOTE) # Right index
    pygame.draw.rect(WINDOW, (191, 197, 199), RIGHT_MIDDLE_NOTE) # Right middle
    pygame.draw.rect(WINDOW, (191, 197, 199), RIGHT_RING_NOTE) # Right ring
    pygame.draw.rect(WINDOW, (191, 197, 199), RIGHT_PINKY_NOTE) # Right pinky

    # Notes
    for i in notes:
        pygame.draw.rect(WINDOW, (255, 255, 255), i[0])
        WINDOW.blit(i[1], (i[0].x + 20, i[0].y + 20))

    # UI
    WINDOW.blit(UI_FONT.render("Score: " + str(score), 0, (0, 0, 0)), (10, 10))
    WINDOW.blit(UI_FONT.render("Multiplier: " + str(multiplier), 0, (0, 0, 0)), (200, 10))
    WINDOW.blit(UI_FONT.render("Difficulty: " + str(difficulty), 0, (0, 0, 0)), (400, 10))

    pygame.display.update()

def process_click(keys_pressed, notes):
    global score, notesHit, multiplier

    if keys_pressed[pygame.K_a]:
        for i in notes:
            if LEFT_PINKY_NOTE.colliderect(i[0]):
                notes.remove(i)
                score = score + (10 * multiplier)
                notesHit = notesHit + 1
    if keys_pressed[pygame.K_s]:
        for i in notes:
            if LEFT_RING_NOTE.colliderect(i[0]):
                notes.remove(i)
                score = score + (10 * multiplier)
                notesHit = notesHit + 1
    if keys_pressed[pygame.K_d]:
        for i in notes:
            if LEFT_MIDDLE_NOTE.colliderect(i[0]):
                notes.remove(i)
                score = score + (10 * multiplier)
                notesHit = notesHit + 1
    if keys_pressed[pygame.K_f]:
        for i in notes:
            if LEFT_INDEX_NOTE.colliderect(i[0]):
                notes.remove(i)
                score = score + (10 * multiplier)
                notesHit = notesHit + 1
    if keys_pressed[pygame.K_j]:
        for i in notes:
            if RIGHT_INDEX_NOTE.colliderect(i[0]):
                notes.remove(i)
                score = score + (10 * multiplier)
                notesHit = notesHit + 1
    if keys_pressed[pygame.K_k]:
        for i in notes:
            if RIGHT_MIDDLE_NOTE.colliderect(i[0]):
                notes.remove(i)
                score = score + (10 * multiplier)
                notesHit = notesHit + 1
    if keys_pressed[pygame.K_l]:
        for i in notes:
            if RIGHT_RING_NOTE.colliderect(i[0]):
                notes.remove(i)
                score = score + (10 * multiplier)
                notesHit = notesHit + 1
    if keys_pressed[pygame.K_SEMICOLON]:
        for i in notes:
            if RIGHT_PINKY_NOTE.colliderect(i[0]):
                notes.remove(i)
                score = score + (10 * multiplier)
                notesHit = notesHit + 1
    
    # Adjust multiplier
    if notesHit >= 5 * multiplier:
        notesHit = 0
        if multiplier < MULTIPLIER_MAX:
            multiplier = multiplier + 1


def move_notes(notes, note_speed, difficulty):
    global score, notesHit, multiplier
    rng = 0

    # Create new note
    if difficulty == "Easy":
        rng = random.randint(0, 1000)
    elif difficulty == "Normal":
        rng = random.randint(0, 500)
    elif difficulty == "Hard":
        rng = random.randint(0, 100)
    else:
        rng = random.randint(1, 8) * 10
    
    if rng == 10:
        note = (pygame.Rect(LEFT_PINKY_NOTE.x, 500, 50, 50), TEXT_FONT.render("A", 1, (0, 0, 0)))
        notes.append(note)
    elif rng == 20:
        note = (pygame.Rect(LEFT_RING_NOTE.x, 500, 50, 50), TEXT_FONT.render("S", 1, (0, 0, 0)))
        notes.append(note)
    elif rng == 30:
        note = (pygame.Rect(LEFT_MIDDLE_NOTE.x, 500, 50, 50), TEXT_FONT.render("D", 1, (0, 0, 0)))
        notes.append(note)
    elif rng == 40:
        note = (pygame.Rect(LEFT_INDEX_NOTE.x, 500, 50, 50), TEXT_FONT.render("F", 1, (0, 0, 0)))
        notes.append(note)
    elif rng == 50:
        note = (pygame.Rect(RIGHT_INDEX_NOTE.x, 500, 50, 50), TEXT_FONT.render("J", 1, (0, 0, 0)))
        notes.append(note)
    elif rng == 60:
        note = (pygame.Rect(RIGHT_MIDDLE_NOTE.x, 500, 50, 50), TEXT_FONT.render("K", 1, (0, 0, 0)))
        notes.append(note)
    elif rng == 70:
        note = (pygame.Rect(RIGHT_RING_NOTE.x, 500, 50, 50), TEXT_FONT.render("L", 1, (0, 0, 0)))
        notes.append(note)
    elif rng == 80:
        note = (pygame.Rect(RIGHT_PINKY_NOTE.x, 500, 50, 50), TEXT_FONT.render(";", 1, (0, 0, 0)))
        notes.append(note)

    # Move note
    for i in notes:
        if i[0].y == 0:
            notes.remove(i)
            if score > 50:
                score = score - 50
            else:
                score = 0
            notesHit = 0
            multiplier = MULTIPLIER_MIN
        else:
            i[0].y -= note_speed


if __name__ == "__main__":
    main()