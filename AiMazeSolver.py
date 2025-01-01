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

def generate_maze():
    maze = [[1 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    stack = [(1, 1)]
    maze[1][1] = 0  # Start with an open cell

    while stack:
        x, y = stack[-1]
        neighbors = [
            (x + dx, y + dy)
            for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]
            if 1 <= x + dx < GRID_SIZE - 1 and 1 <= y + dy < GRID_SIZE - 1 and maze[y + dy][x + dx] == 1
        ]
        if neighbors:
            nx, ny = random.choice(neighbors)
            maze[(y + ny) // 2][(x + nx) // 2] = 0
            maze[ny][nx] = 0
            stack.append((nx, ny))
        else:
            stack.pop()

    return maze

# Modify draw_grid to render the maze
def draw_maze(maze):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            color = BLACK if maze[y][x] == 1 else WHITE
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_button():
    pygame.draw.rect(screen, (0, 128, 255), (WINDOW_SIZE // 3, WINDOW_SIZE - 50, WINDOW_SIZE // 3, 50))
    font = pygame.font.SysFont(None, 36)
    text = font.render("Generate Maze", True, WHITE)
    screen.blit(text, (WINDOW_SIZE // 2 - 80, WINDOW_SIZE - 40))

# Main loop
maze = generate_maze()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if WINDOW_SIZE - 50 <= y <= WINDOW_SIZE and WINDOW_SIZE // 3 <= x <= 2 * WINDOW_SIZE // 3:
                maze = generate_maze()  # Generate a new maze

    screen.fill(BLACK)
    draw_maze(maze)
    draw_button()
    pygame.display.flip()
