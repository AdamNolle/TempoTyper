import pygame
import random

pygame.font.init()

WIDTH, HEIGHT = 700, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
BG = (5, 183, 237)
FPS = 60

TEXT_FONT = pygame.font.SysFont("ariel", 20)
LEFT_PINKY_NOTE = pygame.Rect(10, 50, 50, 50)
LEFT_RING_NOTE = pygame.Rect(80, 50, 50, 50)
LEFT_MIDDLE_NOTE = pygame.Rect(150, 50, 50, 50)
LEFT_INDEX_NOTE = pygame.Rect(220, 50, 50, 50)
RIGHT_INDEX_NOTE = pygame.Rect(430, 50, 50, 50)
RIGHT_MIDDLE_NOTE = pygame.Rect(500, 50, 50, 50)
RIGHT_RING_NOTE = pygame.Rect(570, 50, 50, 50)
RIGHT_PINKY_NOTE = pygame.Rect(640, 50, 50, 50)

pygame.display.set_caption("This is a prototype")

def main():
    global BG
    run = True
    clock = pygame.time.Clock()

    notes = []
    note_speed = 5
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                keys_pressed = pygame.key.get_pressed()
                process_click(keys_pressed, notes)
        move_notes(notes, note_speed)
        draw_window(notes)
    
    pygame.quit()

def draw_window(notes): # Graphic design is my passion
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

    pygame.display.update()

def process_click(keys_pressed, notes):
    if keys_pressed[pygame.K_a]:
        for i in notes:
            if LEFT_PINKY_NOTE.colliderect(i[0]):
                notes.remove(i)
    if keys_pressed[pygame.K_s]:
        for i in notes:
            if LEFT_RING_NOTE.colliderect(i[0]):
                notes.remove(i)
    if keys_pressed[pygame.K_d]:
        for i in notes:
            if LEFT_MIDDLE_NOTE.colliderect(i[0]):
                notes.remove(i)
    if keys_pressed[pygame.K_f]:
        for i in notes:
            if LEFT_INDEX_NOTE.colliderect(i[0]):
                notes.remove(i)
    if keys_pressed[pygame.K_j]:
        for i in notes:
            if RIGHT_INDEX_NOTE.colliderect(i[0]):
                notes.remove(i)
    if keys_pressed[pygame.K_k]:
        for i in notes:
            if RIGHT_MIDDLE_NOTE.colliderect(i[0]):
                notes.remove(i)
    if keys_pressed[pygame.K_l]:
        for i in notes:
            if RIGHT_RING_NOTE.colliderect(i[0]):
                notes.remove(i)
    if keys_pressed[pygame.K_SEMICOLON]:
        for i in notes:
            if RIGHT_PINKY_NOTE.colliderect(i[0]):
                notes.remove(i)


def move_notes(notes, note_speed):
    # Create new note
    rng = random.randint(0, 1000)
    if rng == 100:
        note = (pygame.Rect(LEFT_PINKY_NOTE.x, 500, 50, 50), TEXT_FONT.render("A", 1, (0, 0, 0)))
        notes.append(note)
    elif rng == 200:
        note = (pygame.Rect(LEFT_RING_NOTE.x, 500, 50, 50), TEXT_FONT.render("S", 1, (0, 0, 0)))
        notes.append(note)
    elif rng == 300:
        note = (pygame.Rect(LEFT_MIDDLE_NOTE.x, 500, 50, 50), TEXT_FONT.render("D", 1, (0, 0, 0)))
        notes.append(note)
    elif rng == 400:
        note = (pygame.Rect(LEFT_INDEX_NOTE.x, 500, 50, 50), TEXT_FONT.render("F", 1, (0, 0, 0)))
        notes.append(note)
    elif rng == 500:
        note = (pygame.Rect(RIGHT_INDEX_NOTE.x, 500, 50, 50), TEXT_FONT.render("J", 1, (0, 0, 0)))
        notes.append(note)
    elif rng == 600:
        note = (pygame.Rect(RIGHT_MIDDLE_NOTE.x, 500, 50, 50), TEXT_FONT.render("K", 1, (0, 0, 0)))
        notes.append(note)
    elif rng == 700:
        note = (pygame.Rect(RIGHT_RING_NOTE.x, 500, 50, 50), TEXT_FONT.render("L", 1, (0, 0, 0)))
        notes.append(note)
    elif rng == 800:
        note = (pygame.Rect(RIGHT_PINKY_NOTE.x, 500, 50, 50), TEXT_FONT.render(";", 1, (0, 0, 0)))
        notes.append(note)

    # Move note
    for i in notes:
        if i[0].y == 0:
            notes.remove(i)
        else:
            i[0].y -= note_speed


if __name__ == "__main__":
    main()