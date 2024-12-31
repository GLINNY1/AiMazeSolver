import pygame

# Grid Sizing
WINDOW_SIZE = 800
GRID_SIZE = 40
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialization of Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Maze Setup Step 1")

# Draw an empty grid
def draw_grid():
    for x in range(0, WINDOW_SIZE, CELL_SIZE):
        for y in range(0, WINDOW_SIZE, CELL_SIZE):
            pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE), 1)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    draw_grid()
    pygame.display.flip()

pygame.quit()
