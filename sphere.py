import random
from OpenGL.GL import *
from OpenGL.GLUT import *
import vector3d


class Sphere(object):
    def __init__(self, elasticity, friction):
        self.size = 10
        self.mass = 1.0

        self.colour = vector3d.Vector3D(0.0, 0.0, 0.0)

        self.position = vector3d.Vector3D(0.0, 0.0, 0.0)
        self.previous_position = self.position
        self.velocity = vector3d.Vector3D(0.0, 0.0, 0.0)

        self.elasticity = elasticity
        self.friction = friction

    @staticmethod
    def get_random_size(max_size):
        return random.randint(10, max_size)

    def reset_size(self, max_size):
        self.size = self.get_random_size(max_size)

    @staticmethod
    def get_random_mass(max_mass):
        return random.uniform(1.0, max_mass)

    def reset_mass(self, max_mass):
        self.mass = self.get_random_mass(max_mass)

    @staticmethod
    def get_random_colour():
        return vector3d.Vector3D(random.random(), random.random(), random.random())

    def reset_colour(self):
        self.colour = self.get_random_colour()

    def get_random_position(self, box_size):
        return vector3d.Vector3D(random.uniform(-box_size + self.size, box_size - self.size),
                                 random.uniform(0, box_size - self.size),
                                 random.uniform(-box_size + self.size, box_size - self.size))

    def ball_collision_detection(self, ball):
        return self.position.dot(ball.position) < self.size + ball.size

    def reset_position(self, box_size, balls):
        colliding = True

        while colliding:
            colliding = False

            self.position = self.get_random_position(box_size)

            for ball in balls:
                if ball != self:
                    if self.ball_collision_detection(ball):
                        colliding = True

    @staticmethod
    def get_random_velocity(box_size):
        return vector3d.Vector3D(random.uniform(-box_size, box_size) * 2.0,
                                 0.0,
                                 random.uniform(-box_size, box_size) * 2.0)

    def reset_velocity(self, box_size):
        self.velocity = self.get_random_velocity(box_size)

    def reset(self, max_size, max_mass, box_size, balls):
        self.reset_size(max_size)
        self.reset_mass(max_mass)

        self.reset_colour()
        self.reset_position(box_size, balls)
        self.reset_velocity(box_size)

    @staticmethod
    def integrate(value, increment, delta_time):
        new_value = vector3d.Vector3D(0, 0, 0)

        new_value.x = value.x + (increment.x * delta_time)
        new_value.y = value.y + (increment.y * delta_time)
        new_value.z = value.z + (increment.z * delta_time)

        return new_value

    def box_elastic_constant(self, box):
        return (self.elasticity + box.elasticity) * 0.5

    def box_friction_constant(self, box):
        return 1 - ((self.friction + box.friction) * 0.5)

    def box_collision(self, box):
        if self.position.x - self.size < -box.size or self.position.x + self.size > box.size:
            self.position = self.previous_position

            self.velocity.x *= -1

            self.velocity.x *= self.box_elastic_constant(box)
            self.velocity.y *= self.box_friction_constant(box)
            self.velocity.z *= self.box_friction_constant(box)

        if self.position.y - self.size < -box.size or self.position.y + self.size > box.size:
            self.position = self.previous_position

            self.velocity.y *= -1

            self.velocity.x *= self.box_friction_constant(box)
            self.velocity.y *= self.box_elastic_constant(box)
            self.velocity.z *= self.box_friction_constant(box)

        if self.position.z - self.size < -box.size or self.position.z + self.size > box.size:
            self.position = self.previous_position

            self.velocity.z *= -1

            self.velocity.x *= self.box_friction_constant(box)
            self.velocity.y *= self.box_friction_constant(box)
            self.velocity.z *= self.box_elastic_constant(box)

    def ball_elastic_constant(self, ball):
        return (self.elasticity + ball.elasticity) * 0.5

    def ball_collision_response(self, ball):
        if self.ball_collision_detection(ball):
            normal = vector3d.Vector3D(self.position.x - ball.position.x,
                                       self.position.y - ball.position.y,
                                       self.position.z - ball.position.z)

            normal.normalise()

            force_magnitude = ((self.velocity.dot(normal) - ball.velocity.dot(normal)) * 2.0) / (self.mass + ball.mass)

            self.velocity = vector3d.Vector3D(self.velocity.x - ((force_magnitude * ball.mass) * normal.x),
                                              self.velocity.y - ((force_magnitude * ball.mass) * normal.y),
                                              self.velocity.z - ((force_magnitude * ball.mass) * normal.z))

            ball.velocity = vector3d.Vector3D(ball.velocity.x + ((force_magnitude * self.mass) * normal.x),
                                              ball.velocity.y + ((force_magnitude * self.mass) * normal.y),
                                              ball.velocity.z + ((force_magnitude * self.mass) * normal.z))

            self.velocity.x *= normal.x * self.ball_elastic_constant(ball)
            self.velocity.y *= normal.y * self.ball_elastic_constant(ball)
            self.velocity.z *= normal.z * self.ball_elastic_constant(ball)

            ball.velocity.x *= normal.x * ball.ball_elastic_constant(self)
            ball.velocity.y *= normal.y * ball.ball_elastic_constant(self)
            ball.velocity.z *= normal.z * ball.ball_elastic_constant(self)

            self.position = self.previous_position
            ball.position = ball.previous_position

            midpoint = vector3d.Vector3D((self.position.x - ball.position.x) * 0.1,
                                         (self.position.y - ball.position.y) * 0.1,
                                         (self.position.z - ball.position.z) * 0.1)

            while self.ball_collision_detection(ball):
                self.position.x += midpoint.x
                self.position.y += midpoint.y
                self.position.z += midpoint.z

                ball.position.x -= midpoint.x
                ball.position.y -= midpoint.y
                ball.position.z -= midpoint.z

    def check_moving(self, max_size, max_mass, box_size, balls):
        if self.velocity.magnitude() < 100:
            self.reset(max_size, max_mass, box_size, balls)

    def update(self, delta_time, force, box):
        self.previous_position = self.position

        self.velocity = self.integrate(self.velocity, force, delta_time)
        self.position = self.integrate(self.position, self.velocity, delta_time)

        self.box_collision(box)

    def draw(self):
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [self.colour.x, self.colour.y, self.colour.z, 1.0])
        glMaterialfv(GL_FRONT, GL_SPECULAR, [1, 1, 1, 1])
        glMaterialfv(GL_FRONT, GL_SHININESS, [100.0])

        glPushMatrix()

        glTranslatef(self.position.x, self.position.y, self.position.z)

        glutSolidSphere(self.size, self.size, self.size)

        glPopMatrix()
