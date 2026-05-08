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
# MAZE STRUCTURES
northWall = [[1 for _ in range(C)] for _ in range(R + 1)]
eastWall = [[1 for _ in range(C + 1)] for _ in range(R)]

visited = [[False for _ in range(C)] for _ in range(R)]
# GENERATION STATE
stack = []
current_cell = (0, 0)
visited[0][0] = True
generating = True
solving = False
# SOLVER STATE
direction = 1
mouse_position = (R - 1, 0)
path = []
dead_ends = set()
visited_solver = set()
ENABLE_CYCLES = True
# OPENGL INIT
def init():
    glClearColor(0, 0, 0, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)
# DRAW MAZE
def draw_maze():
    glColor3f(1, 1, 1)
    glLineWidth(2)
    glBegin(GL_LINES)

    for r in range(R):
        for c in range(C):

            y = (R - r - 1) * CELL_SIZE

            if northWall[r][c]:
                glVertex2f(c * CELL_SIZE, y + CELL_SIZE)
                glVertex2f((c + 1) * CELL_SIZE, y + CELL_SIZE)

            if eastWall[r][c]:
                glVertex2f((c + 1) * CELL_SIZE, y)
                glVertex2f((c + 1) * CELL_SIZE, y + CELL_SIZE)

    glEnd()
# DRAW ENTITIES
def draw_entities():
    glEnable(GL_POINT_SMOOTH)

    # PATH
    glColor3f(1, 0, 0)
    glPointSize(6)
    glBegin(GL_POINTS)
    for r, c in path:
        y = (R - r - 1) * CELL_SIZE
        glVertex2f(c * CELL_SIZE + CELL_SIZE / 2, y + CELL_SIZE / 2)
    glEnd()

    # DEAD ENDS
    glColor3f(0, 0, 1)
    glPointSize(8)
    glBegin(GL_POINTS)
    for r, c in dead_ends:
        y = (R - r - 1) * CELL_SIZE
        glVertex2f(c * CELL_SIZE + CELL_SIZE / 2, y + CELL_SIZE / 2)
    glEnd()

    # MOUSE
    r, c = mouse_position
    y = (R - r - 1) * CELL_SIZE
    glColor3f(0, 1, 0)
    glPointSize(12)
    glBegin(GL_POINTS)
    glVertex2f(c * CELL_SIZE + CELL_SIZE / 2, y + CELL_SIZE / 2)
    glEnd()

# MAZE GENERATION
def generate_step():
    global current_cell, generating, solving

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
        nr, nc, d = random.choice(neighbors)
        stack.append(current_cell)

        if d == 'N':
            northWall[r][c] = 0
        elif d == 'S':
            northWall[r - 1][c] = 0
        elif d == 'E':
            eastWall[r][c] = 0
        elif d == 'W':
            eastWall[r][c - 1] = 0

        visited[nr][nc] = True
        current_cell = (nr, nc)

    elif stack:
        current_cell = stack.pop()

    else:
        generating = False

        # entrance + exit
        eastWall[R - 1][0] = 0
        eastWall[0][C - 1] = 0

        # BONUS CYCLES FIXED
        if ENABLE_CYCLES:
            for _ in range((R * C) // 20):
                r = random.randint(0, R - 2)
                c = random.randint(0, C - 2)

                if random.choice([True, False]):
                    northWall[r][c] = 0
                else:
                    eastWall[r][c] = 0

        solving = True
# WALL CHECK

def can_move(r, c, d):
    if d == 0 and r < R - 1 and northWall[r][c] == 0:
        return True
    if d == 1 and c < C - 1 and eastWall[r][c] == 0:
        return True
    if d == 2 and r > 0 and northWall[r - 1][c] == 0:
        return True
    if d == 3 and c > 0 and eastWall[r][c - 1] == 0:
        return True
    return False

def move_forward(r, c, d):
    if d == 0:
        return (r + 1, c)
    if d == 1:
        return (r, c + 1)
    if d == 2:
        return (r - 1, c)
    return (r, c - 1)

# SOLVER
def solve_step():
    global mouse_position, direction, solving

    r, c = mouse_position
    path.append((r, c))

    if (r, c) == (0, C - 1):
        solving = False
        return

    priorities = [
        (direction + 1) % 4,
        direction,
        (direction - 1) % 4,
        (direction + 2) % 4
    ]

    for nd in priorities:
        if can_move(r, c, nd):
            direction = nd
            mouse_position = move_forward(r, c, nd)
            return

    dead_ends.add((r, c))
# DISPLAY
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_maze()
    draw_entities()
    glutSwapBuffers()
# UPDATE LOOP

def update(value):
    if generating:
        generate_step()
    elif solving:
        solve_step()

    glutPostRedisplay()
    glutTimerFunc(20, update, 0)
# MAIN

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow(b"Maze Generator + Solver")

    init()
    glutDisplayFunc(display)
    glutTimerFunc(20, update, 0)
    glutMainLoop()
# ENTRY

if __name__ == "__main__":
    main()