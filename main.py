from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import spheres
import cube


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glOrtho(0.0, width, 0.0, height, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glColor3f(1.0, 1.0, 1.0)

    box.update()
    box.draw()

    #ball_list.update(box)
    #ball_list.draw()

    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)

    glutInitWindowSize(1600, 900)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("python_simulation_opengl")

    glutDisplayFunc(draw)
    glutIdleFunc(draw)

    glutMainLoop()


height = 900
width = 1600

box = cube.Cube()
ball_list = spheres.Spheres()

main()
