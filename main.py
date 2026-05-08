import random
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# CONFIGURATION
R, C = 20, 25
CELL_SIZE = 30
WINDOW_WIDTH = C * CELL_SIZE
WINDOW_HEIGHT = R * CELL_SIZE
# MAZE DATA STRUCTURES
northWall = [[1 for _ in range(C)] for _ in range(R + 1)]
eastWall = [[1 for _ in range(C + 1)] for _ in range(R)]

visited = [[False for _ in range(C)] for _ in range(R)]
# DFS STATE

stack = []
current_cell = (0, 0)
visited[0][0] = True

# MAZE GENERATION FUNCTION (DFS)

def generate_step():

    global current_cell

    r, c = current_cell

    neighbors = []

    # Check all 4 directions

    # NORTH
    if r < R - 1 and not visited[r + 1][c]:
        neighbors.append((r + 1, c, 'N'))

    # SOUTH
    if r > 0 and not visited[r - 1][c]:
        neighbors.append((r - 1, c, 'S'))

    # EAST
    if c < C - 1 and not visited[r][c + 1]:
        neighbors.append((r, c + 1, 'E'))

    # WEST
    if c > 0 and not visited[r][c - 1]:
        neighbors.append((r, c - 1, 'W'))

    # If we have available moves
    if neighbors:

        nr, nc, direction = random.choice(neighbors)

        # push current cell to stack for backtracking
        stack.append(current_cell)

        # REMOVE WALLS BETWEEN CELLS

        if direction == 'N':
            northWall[r][c] = 0

        elif direction == 'S':
            northWall[r - 1][c] = 0

        elif direction == 'E':
            eastWall[r][c] = 0

        elif direction == 'W':
            eastWall[r][c - 1] = 0

        # move to new cell
        visited[nr][nc] = True
        current_cell = (nr, nc)
    # BACKTRACK
    elif stack:
        current_cell = stack.pop()

# OPENGL INIT

def init():
    glClearColor(0, 0, 0, 1)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)
# DISPLAY (EMPTY FOR NOW - RENDER ADDED NEXT COMMIT)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glutSwapBuffers()
# UPDATE LOOP (RUNS DFS STEP BY STEP)

def update(value):

    generate_step()

    glutPostRedisplay()

    glutTimerFunc(10, update, 0)
# MAIN
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow(b"Maze Generator - DFS")
    init()

    glutDisplayFunc(display)

    glutTimerFunc(10, update, 0)

    glutMainLoop()

# ENTRY

if __name__ == "__main__":
    main()