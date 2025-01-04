import pygame
import random
from collections import deque

# Constants
WINDOW_SIZE = 800
BUTTON_HEIGHT = 50
GRID_SIZE = 40
CELL_SIZE = WINDOW_SIZE // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BUTTON_COLOR = (0, 128, 255)

# Font
FONT_SIZE = 20

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + BUTTON_HEIGHT))
pygame.display.set_caption("AI-Powered Maze Solver")
font = pygame.font.SysFont(None, FONT_SIZE)

# Helper Functions
def random_border_point(exclude=None, min_distance=2):
    """Generate a random point on the border, ensuring minimum distance from an excluded point."""
    while True:
        borders = (
            [(x, 0) for x in range(GRID_SIZE)] +
            [(x, GRID_SIZE - 1) for x in range(GRID_SIZE)] +
            [(0, y) for y in range(GRID_SIZE)] +
            [(GRID_SIZE - 1, y) for y in range(GRID_SIZE)]
        )
        point = random.choice(borders)
        if not exclude or abs(point[0] - exclude[0]) + abs(point[1] - exclude[1]) >= min_distance:
            return point

def is_solvable(maze, start, end):
    """Check if the maze is solvable using BFS."""
    queue = deque([start])
    visited = set(queue)

    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            return True

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and maze[ny][nx] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))

    return False

def generate_maze():
    """Generate a random solvable maze."""
    while True:
        maze = [[1 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

        start_point = random_border_point()
        end_point = random_border_point(exclude=start_point)

        maze[start_point[1]][start_point[0]] = 0
        maze[end_point[1]][end_point[0]] = 0

        stack = [(1, 1)]
        while stack:
            x, y = stack[-1]
            maze[y][x] = 0

            neighbors = [
                (x + dx, y + dy)
                for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]
                if 1 <= x + dx < GRID_SIZE - 1 and 1 <= y + dy < GRID_SIZE - 1 and maze[y + dy][x + dx] == 1
            ]

            if neighbors:
                nx, ny = random.choice(neighbors)
                maze[(y + ny) // 2][(x + nx) // 2] = 0
                stack.append((nx, ny))
            else:
                stack.pop()

        if is_solvable(maze, start_point, end_point):
            return maze, start_point, end_point

def bfs_solve(maze, start, end):
    """Solve the maze using BFS and visualize the process."""
    queue = deque([start])
    visited = set(queue)
    parents = {}

    while queue:
        x, y = queue.popleft()

        pygame.draw.rect(screen, GREEN, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.display.flip()
        pygame.time.delay(20)

        if (x, y) == end:
            # Highlight the optimal path
            while (x, y) != start:
                pygame.draw.rect(screen, BLUE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.display.flip()
                pygame.time.delay(50)
                x, y = parents[(x, y)]
            return True

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and maze[ny][nx] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                parents[(nx, ny)] = (x, y)
                queue.append((nx, ny))

    return False

def draw_maze(maze, start, end):
    """Render the maze with start and end points."""
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            color = BLACK if maze[y][x] == 1 else WHITE
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.draw.rect(screen, GREEN, (start[0] * CELL_SIZE, start[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (end[0] * CELL_SIZE, end[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_buttons():
    """Render the control buttons."""
    pygame.draw.rect(screen, GREEN, (0, WINDOW_SIZE, WINDOW_SIZE // 3, BUTTON_HEIGHT))
    pygame.draw.rect(screen, BUTTON_COLOR, (WINDOW_SIZE // 3, WINDOW_SIZE, WINDOW_SIZE // 3, BUTTON_HEIGHT))
    pygame.draw.rect(screen, RED, (2 * WINDOW_SIZE // 3, WINDOW_SIZE, WINDOW_SIZE // 3, BUTTON_HEIGHT))

    screen.blit(font.render("Start", True, WHITE), (WINDOW_SIZE // 6 - 20, WINDOW_SIZE + 10))
    screen.blit(font.render("Randomize", True, WHITE), (WINDOW_SIZE // 2 - 50, WINDOW_SIZE + 10))
    screen.blit(font.render("Quit", True, WHITE), (5 * WINDOW_SIZE // 6 - 20, WINDOW_SIZE + 10))

def main():
    """Main game loop."""
    maze, start_point, end_point = generate_maze()
    running = True
    solved = False

    while running:
        screen.fill(WHITE)
        draw_maze(maze, start_point, end_point)
        draw_buttons()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if y > WINDOW_SIZE:
                    if x < WINDOW_SIZE // 3:  # Start button
                        solved = bfs_solve(maze, start_point, end_point)
                    elif x < 2 * WINDOW_SIZE // 3:  # Randomize button
                        maze, start_point, end_point = generate_maze()
                        solved = False
                    elif x < WINDOW_SIZE:  # Quit button
                        running = False

        if solved:
            continue

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
