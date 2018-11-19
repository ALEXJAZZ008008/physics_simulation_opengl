from OpenGL.GL import *
from OpenGL.GLUT import *
import delta_time
import constants
import spheres
import cube
import camera


def display():
    delta_time.update_current_time()
    delta_time.update_delta_time()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    if keyboard_camera.rotation_bool:
        glRotatef(keyboard_camera.rotation_magnitude.x, keyboard_camera.rotation_direction.x, 0.0, 0.0)
        glRotatef(keyboard_camera.rotation_magnitude.y, 0.0, keyboard_camera.rotation_direction.y, 0.0)
        glRotatef(keyboard_camera.rotation_magnitude.z, 0.0, 0.0, keyboard_camera.rotation_direction.z)

        keyboard_camera.reset_rotation()

        keyboard_camera.rotation_bool = False

    if keyboard_camera.translation_bool:
        glTranslatef(keyboard_camera.translation.x, keyboard_camera.translation.y, 0.0)
        glScalef(keyboard_camera.translation.z, keyboard_camera.translation.z, keyboard_camera.translation.z)

        keyboard_camera.reset_translation()

        keyboard_camera.translation_bool = False

    box.update()
    box.draw()

    ball_list.update(delta_time.delta_time * keyboard_camera.speed, constants.gravitational_acceleration(), box)
    ball_list.draw()

    glFlush()
    glutSwapBuffers()
    glutPostRedisplay()

    delta_time.update_previous_time()


def keyboard(key, i, j):
    if key == b'w':
        keyboard_camera.rotation_magnitude.x = -1.0
        keyboard_camera.rotation_direction.x = 1.0

        keyboard_camera.rotation_bool = True
    elif key == b's':
        keyboard_camera.rotation_magnitude.x = 1.0
        keyboard_camera.rotation_direction.x = 1.0

        keyboard_camera.rotation_bool = True
    elif key == b'a':
        keyboard_camera.rotation_magnitude.y = 1.0
        keyboard_camera.rotation_direction.y = 1.0

        keyboard_camera.rotation_bool = True
    elif key == b'd':
        keyboard_camera.rotation_magnitude.y = -1.0
        keyboard_camera.rotation_direction.y = 1.0

        keyboard_camera.rotation_bool = True
    elif key == b'e':
        keyboard_camera.rotation_magnitude.z = 1.0
        keyboard_camera.rotation_direction.z = 1.0

        keyboard_camera.rotation_bool = True
    elif key == b'q':
        keyboard_camera.rotation_magnitude.z = -1.0
        keyboard_camera.rotation_direction.z = 1.0

        keyboard_camera.rotation_bool = True
    elif key == b'i':
        keyboard_camera.translation.y = 100.0

        keyboard_camera.translation_bool = True
    elif key == b'k':
        keyboard_camera.translation.y = -100.0

        keyboard_camera.translation_bool = True
    elif key == b'j':
        keyboard_camera.translation.x = 100.0

        keyboard_camera.translation_bool = True
    elif key == b'l':
        keyboard_camera.translation.x = -100.0

        keyboard_camera.translation_bool = True
    elif key == b'o':
        keyboard_camera.translation.z = 1.1

        keyboard_camera.translation_bool = True
    elif key == b'u':
        keyboard_camera.translation.z = 0.9

        keyboard_camera.translation_bool = True
    elif key == b't':
        keyboard_camera.speed += 0.1
    elif key == b'g':
        keyboard_camera.speed -= 0.1


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)

    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("python_simulation_opengl")

    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutKeyboardFunc(keyboard)

    glMatrixMode(GL_PROJECTION)
    glShadeModel(GL_SMOOTH)

    glEnable(GL_DEPTH_TEST)

    glEnable(GL_LIGHTING)

    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.0, 0.0, 0.0, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.7, 0.7, 0.7, 1.0])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [0.7, 0.7, 0.7, 1.0])

    glLightfv(GL_LIGHT0, GL_POSITION, [-500, 1000, -1000, 1])

    glEnable(GL_LIGHT0)

    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.3, 0.3, 0.3, 1.0])
    glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE)

    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)

    glClearColor(0.0, 0.0, 0.0, 0.0)

    glLoadIdentity()
    glOrtho(0.0, width, height, 0.0, -100000.0, 100000.0)
    glPointSize(1.0)

    glTranslatef(width / 2, height / 2, 0.0)
    glScalef(0.25, 0.25, 0.25)
    glRotatef(180.0, 0.0, 0.0, 1.0)
    glRotatef(20.0, 1.0, 1.0, 0.0)

    glutMainLoop()


height = 900
width = 1600

keyboard_camera = camera.Camera()

box = cube.Cube(1000, constants.cube_indices(), 0.8, 0.2)
ball_list = spheres.Spheres(20, 125, 2.0, box.size, 0.8, 0.2)

delta_time = delta_time.DeltaTime()

main()
