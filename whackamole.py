import pygame
import random

cols = 20
rows = 16
size = 32
width = cols * size
height = rows * size

def draw_lines_grid(screen):
    for x in range(0, width, size):
        pygame.draw.line(screen, "black", (x, 0), (x, height))
    for y in range(0, height, size):
        pygame.draw.line(screen, "black", (0, y), (width, y))

def change_move():
    mole_x_pos = random.randint(0, cols - 1) * size
    mole_y_pos = random.randint(0, rows - 1) * size
    return mole_x_pos, mole_y_pos




def main():
    try:
        pygame.init() #initializes pygame

        mole_image = pygame.image.load("mole.png")
        mole_image = pygame.transform.scale(mole_image, (size, size))
        screen = pygame.display.set_mode((width, height)) #defining how large the window will be when you play
        clock = pygame.time.Clock()
        mole_x_pos, mole_y_pos = change_move()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if mole_x_pos <= x < (mole_x_pos * size) and mole_y_pos <= y < (mole_y_pos * size):
                        mole_x_pos, mole_y_pos = change_move()
            screen.fill("light green") #background color
            draw_lines_grid(screen)
            screen.blit(mole_image, (mole_x_pos, mole_y_pos))        # You can draw the mole with this snippet:
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
