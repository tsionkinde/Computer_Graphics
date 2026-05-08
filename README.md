## Maze Generator & Solver (PyOpenGL)

This project is a visual simulation of a Maze Generator and Solver built using Python and PyOpenGL. It demonstrates how a maze can be created using the Depth-First Search (DFS) Recursive Backtracking algorithm, and then solved automatically using a wall-following (right-hand rule) algorithm.

The program runs in real-time and visually shows how the maze is formed step by step, followed by how the solver navigates through it.

## Features
* Random maze generation using DFS Backtracking
* Real-time visualization of maze creation
* Automatic maze solving using wall-following algorithm
* Dead-end detection and visualization
* Live mouse/agent movement during solving phase
* Automatic entrance and exit creation
* Optional cycle generation (adds complexity to maze)
* Smooth animation using GLUT timer updates
## How It Works
1. Maze Generation (DFS Backtracking)
The maze is generated using a stack-based Depth-First Search algorithm:
Start from a cell
Randomly visit unvisited neighbors
Remove walls between cells
Backtrack using a stack when no moves are available
This creates a perfect maze (initially without loops).
2.  Cycle Creation
After generation, some random walls are removed (about 1 in 20 cells) to:
Introduce loops (cycles)
Make the maze more realistic and complex
Break the strict “single path” structure
3. Maze Solving
The solver uses a Wall-Following (Right-Hand Rule) algorithm:
Always tries to turn right first
Then forward, left, and back
Tracks visited paths and dead ends
Finds path from entrance to exit automatically
4. Visualization
The program visually represents:
* White lines → Maze walls
* Red dots → Path taken
* Blue dots → Dead ends
* Green dot → Current position of solver
   ## Technologies Used
Python 3
PyOpenGL
GLUT (OpenGL Utility Toolkit)
OpenGL (GL, GLU)
# Project Structure
Computer Graphics
│
├── main.py              # Maze generator + solver (core logic)
├── README.md            # Project documentation

## How to Run
1. Install dependencies
pip install PyOpenGL PyOpenGL_accelerate
2. Run the program
python main.py
## Key Algorithms Used
Depth-First Search (DFS) Recursive Backtracking → Maze Generation
Stack-based Backtracking → Path exploration
Wall-Following Algorithm → Maze Solving
