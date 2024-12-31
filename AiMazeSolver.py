import pygame
import random

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

# Function to generate random border points
def random_border_point():
    borders = []
    for x in range(GRID_SIZE):
        borders.append((x, 0))  # Top border
        borders.append((x, GRID_SIZE - 1))  # Bottom border
    for y in range(GRID_SIZE):
        borders.append((0, y))  # Left border
        borders.append((GRID_SIZE - 1, y))  # Right border
    return random.choice(borders)

# Modify draw_grid to show start and end points
def draw_grid():
    for x in range(0, WINDOW_SIZE, CELL_SIZE):
        for y in range(0, WINDOW_SIZE, CELL_SIZE):
            pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE), 1)
    pygame.draw.rect(screen, (0, 255, 0), (START_POINT[0] * CELL_SIZE, START_POINT[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, (255, 0, 0), (END_POINT[0] * CELL_SIZE, END_POINT[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Generate start and end points (randomizing them everytime)
START_POINT = random_border_point()
END_POINT = random_border_point()
while START_POINT == END_POINT:  # Ensure start and end are different
    END_POINT = random_border_point()

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
