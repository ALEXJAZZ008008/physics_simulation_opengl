import random
from OpenGL.GL import *
from OpenGL.GLUT import *
import vector3d


class Sphere(object):
    def __init__(self,
                 size=30,
                 gravitational_acceleration=vector3d.Vector3D(0, -9.8, 0),
                 mass=1,
                 elasticity=0.8,
                 friction=0.2
                 ):
        self.size = size

        self.position = vector3d.Vector3D(random.uniform(size, size),
                                          random.uniform((size + size) * 0.5, size),
                                          random.uniform(size, size))

        self.velocity = vector3d.Vector3D(random.uniform(-size, size) * 2,
                                          random.uniform(0, size) * 2,
                                          random.uniform(-size, size) * 2)

        self.force = gravitational_acceleration

        self.mass = mass

        self.elasticity = elasticity
        self.friction = friction

        self.moving = True

    @staticmethod
    def integrate(value, increment, delta_time):
        new_value = vector3d.Vector3D(0, 0, 0)

        new_value.x = value.x + (increment.x * delta_time)
        new_value.y = value.y + (increment.y * delta_time)
        new_value.z = value.z + (increment.z * delta_time)

        return new_value

    def elastic_constant(self, box):
        return (self.elasticity + box.elasticity) * 0.5

    def friction_constant(self, box):
        return 1 - ((self.friction + box.friction) * 0.5)

    def collision(self, box, previous_position):
        if self.position.x < -box.size or self.position.x > box.size:
            self.position = previous_position

            self.velocity.x *= -1

            self.velocity.x *= self.elastic_constant(box)
            self.velocity.y *= self.friction_constant(box)
            self.velocity.z *= self.friction_constant(box)

        if self.position.y < -box.size or self.position.y > box.size:
            self.position = previous_position

            self.velocity.y *= -1

            self.velocity.x *= self.friction_constant(box)
            self.velocity.y *= self.elastic_constant(box)
            self.velocity.z *= self.friction_constant(box)

        if self.position.z < -box.size or self.position.z > box.size:
            self.position = previous_position

            self.velocity.z *= -1

            self.velocity.x *= self.friction_constant(box)
            self.velocity.y *= self.friction_constant(box)
            self.velocity.z *= self.elastic_constant(box)

    def update_moving(self):
        if self.velocity.dot() < 0.1:
            self.velocity = vector3d.Vector3D(0, 0, 0)

            self.moving = False

    def update(self, delta_time, box):
        previous_position = self.position

        self.velocity = self.integrate(self.velocity, self.force, delta_time)
        self.position = self.integrate(self.position, self.velocity, delta_time)

        self.collision(box, previous_position)

        self.update_moving()

    def draw(self):
        glPushMatrix()

        glTranslatef(self.position.x, self.position.y, self.position.z)

        glutSolidSphere(self.size, self.size, self.size)

        glPopMatrix()
