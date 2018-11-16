import sphere


class Spheres(object):
    def __init__(self, number_of_spheres, max_size, max_mass, box_size, elasticity, friction):
        self.balls = []

        self.max_size = max_size
        self.max_mass = max_mass

        for i in range(number_of_spheres):
            self.balls.append(sphere.Sphere(elasticity, friction))

        for ball in self.balls:
            ball.reset(self.max_size, self.max_mass, box_size, self.balls)

    def update(self, delta_time, force, box):
        for ball in self.balls:
            ball.update(delta_time, force, box)

        for i, ball1 in enumerate(self.balls):
            for ball2 in self.balls[i + 1::]:
                ball1.ball_collision_response(ball2)

        for ball in self.balls:
            ball.check_moving(self.max_size, self.max_mass, box.size, self.balls)

    def draw(self):
        for ball in self.balls:
            ball.draw()
