from OpenGL.GL import *


class Cube(object):
    def __init__(self,
                 size=1,
                 indices=(
                         (0, 1),
                         (0, 3),
                         (0, 4),
                         (2, 1),
                         (2, 3),
                         (2, 7),
                         (6, 3),
                         (6, 4),
                         (6, 7),
                         (5, 1),
                         (5, 4),
                         (5, 7)
                 ),
                 elasticity=0.8,
                 friction=0.2
                 ):
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
        glBegin(GL_LINES)

        for index in self.indices:
            for vertex in index:
                glVertex3fv(self.vertices[vertex])

        glEnd()
