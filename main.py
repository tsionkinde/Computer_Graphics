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
# MAZE GENERATION (DFS STEP)
def generate_step():
    global current_cell
    r, c = current_cell
    neighbors = []
    if r < R - 1 and not visited[r + 1][c]:
        neighbors.append((r + 1, c, 'N'))

    if r > 0 and not visited[r - 1][c]:
        neighbors.append((r - 1, c, 'S'))

    if c < C - 1 and not visited[r][c + 1]:
        neighbors.append((r, c + 1, 'E'))

    if c > 0 and not visited[r][c - 1]:
        neighbors.append((r, c - 1, 'W'))

    if neighbors:

        nr, nc, direction = random.choice(neighbors)

        stack.append(current_cell)

        if direction == 'N':
            northWall[r][c] = 0
        elif direction == 'S':
            northWall[r - 1][c] = 0
        elif direction == 'E':
            eastWall[r][c] = 0
        elif direction == 'W':
            eastWall[r][c - 1] = 0

        visited[nr][nc] = True
        current_cell = (nr, nc)

    elif stack:
        current_cell = stack.pop()
# OPENGL INIT
def init():
    glClearColor(0, 0, 0, 1)

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)
# DRAW MAZE WALLS
def draw_maze():
    glColor3f(1, 1, 1)
    glLineWidth(2)
    glBegin(GL_LINES)
    for r in range(R):
        for c in range(C):

            y = (R - r - 1) * CELL_SIZE
            # TOP WALL
            if northWall[r][c]:
                glVertex2f(c * CELL_SIZE, y + CELL_SIZE)
                glVertex2f((c + 1) * CELL_SIZE, y + CELL_SIZE)

            # RIGHT WALL
            if eastWall[r][c]:
                glVertex2f((c + 1) * CELL_SIZE, y)
                glVertex2f((c + 1) * CELL_SIZE, y + CELL_SIZE)

    glEnd()
# DISPLAY
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_maze()
    glutSwapBuffers()
# UPDATE LOOP
def update(value):
    generate_step()
    glutPostRedisplay()
    glutTimerFunc(10, update, 0)
# MAIN
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow(b"Maze Generator - Rendering")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(10, update, 0)
    glutMainLoop()
# ENTRY POINT
if __name__ == "__main__":
    main()