from OpenGL.GL import *


class Cube(object):
    def __init__(self, size, indices, elasticity, friction):
        self.size = size

        self.vertices = (
                         (size, -size, -size),
                         (size, size, -size),
                         (-size, size, -size),
                         (-size, -size, -size),
                         (size, -size, size),
                         (size, size, size),
                         (-size, -size, size),
                         (-size, size, size)
        )
        self.indices = indices

        self.elasticity = elasticity
        self.friction = friction

    def update(self):
        pass

    def draw(self):
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
        glMaterialfv(GL_FRONT, GL_SPECULAR, [1, 1, 1, 1])
        glMaterialfv(GL_FRONT, GL_SHININESS, [100.0])

        glBegin(GL_LINES)

        for index in self.indices:
            for vertex in index:
                glVertex3fv(self.vertices[vertex])

        glEnd()
