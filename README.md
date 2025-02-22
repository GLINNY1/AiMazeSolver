# AI-Powered Maze Solver

## Overview

The **AI-Powered Maze Solver** is an interactive Python project built using Pygame. It generates random mazes and uses AI pathfinding algorithms to solve them. The project demonstrates real-time visualization of maze solving, highlighting the most optimal path to the destination.

## Features

- **Maze Generation**:
  - Uses a depth-first search (DFS) algorithm to generate random mazes.
  - Ensures all mazes are solvable by validating with breadth-first search (BFS).
- **Pathfinding**:
  - Implements a BFS algorithm to solve the maze and find the most optimal path.
  - Visualizes the solving process in real time.
- **Interactive Controls**:
  - Start solving the maze.
  - Generate a new random maze.
  - Quit the application.
- **Graphical Interface**:
  - Displays the maze with start and end points.
  - Highlights the solution path after completion.

## Usage

1. Run the program:
   ```bash
   python maze_solver.py
   ```
2. Interact with the application:
   - **Start**: Solve the current maze.
   - **Randomize**: Generate a new maze.
   - **Quit**: Exit the application.

## Controls

- **Start Button**: Begins solving the current maze and visualizes the process.
- **Randomize Button**: Generates a new maze for solving.
- **Quit Button**: Exits the application.

## How It Works

### Maze Generation

- **Algorithm**: Depth-first search (DFS) with backtracking creates random paths.
- **Validation**: BFS ensures that the maze is solvable by checking connectivity between the start and end points.

### Pathfinding

- **Algorithm**: Breadth-first search (BFS) explores all possible paths to find the shortest route.
- **Visualization**: The solver visually marks cells as it progresses and highlights the optimal path upon completion.

## Project Structure

```
maze-solver/
|-- maze_solver.py   # Main application file
|-- README.md        # Project documentation
```

## Future Enhancements

- Implement additional pathfinding algorithms (e.g., A\*).
- Add adjustable maze sizes and difficulty levels.
- Include a scoring system to evaluate solving efficiency.

## Acknowledgments

- Pygame for the graphical interface.
- Python's built-in libraries for data structure implementations.

