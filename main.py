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
    glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)

    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("python_simulation_opengl")

    glutDisplayFunc(draw)
    glutIdleFunc(draw)

    glClearColor(0.0, 0.0, 0.0, 0.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, height, 0.0, -1000.0, 1000.0)
    glEnable(GL_DEPTH_TEST)

    glTranslatef(width / 2, height / 2, 0.0)
    glRotatef(180.0, 0.0, 0.0, 1.0)
    glRotatef(20.0, 1.0, 1.0, 0.0)

    glutMainLoop()


height = 900
width = 1600

box = cube.Cube()
ball_list = spheres.Spheres()

main()
