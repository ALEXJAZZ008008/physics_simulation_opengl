import sphere


class Spheres(object):
    def __init__(self, number_of_spheres, box_size, size, elasticity, friction):
        self.balls = []

        for i in range(number_of_spheres):
            self.balls.append(sphere.Sphere(box_size, size, elasticity, friction))

        for ball in self.balls:
            ball.reset(box_size, self.balls)

    def update(self, delta_time, force, box):
        for ball in self.balls:
            ball.update(delta_time, force, box)

        for ball in self.balls:
            ball.balls_collision(self.balls)

        for ball in self.balls:
            ball.check_moving(box.size, self.balls)

    def draw(self):
        for ball in self.balls:
            ball.draw()
