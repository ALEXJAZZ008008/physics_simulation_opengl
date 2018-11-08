from OpenGL.GL import *
from OpenGL.GLUT import *
import spheres
import cube


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glColor3f(1.0, 1.0, 1.0)

    box.update()
    box.draw()

    ball_list.update(box)
    ball_list.draw()

    glFlush()
    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)

    glutInitWindowSize(1600, 900)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("python_simulation_opengl")

    glutDisplayFunc(draw)
    glutIdleFunc(draw)

    glClearColor(0.0, 0.0, 0.0, 0.0)
    glPointSize(5.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 550.0, 550.0, 0.0, -100.0, 100.0)
    glEnable(GL_DEPTH_TEST)

    glutMainLoop()


height = 900
width = 1600

box = cube.Cube()
ball_list = spheres.Spheres()

main()
