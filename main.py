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
# northWall[r][c] = top wall of cell (r, c)
# eastWall[r][c] = right wall of cell (r, c)

northWall = [[1 for _ in range(C)] for _ in range(R + 1)]
eastWall = [[1 for _ in range(C + 1)] for _ in range(R)]
# visited[r][c] = used for DFS maze generation
visited = [[False for _ in range(C)] for _ in range(R)]
# DFS MAZE GENERATION STATE (INIT ONLY)
stack = []
current_cell = (0, 0)

# mark starting cell as visited
visited[0][0] = True
# OPENGL INIT
def init():
    glClearColor(0, 0, 0, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)
# DISPLAY FUNCTION (NO MAZE DRAWING YET)
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glutSwapBuffers()
# MAIN
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow(b"Maze Generator")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
# ENTRY
if __name__ == "__main__":
    main()