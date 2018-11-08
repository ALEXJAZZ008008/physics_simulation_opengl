import time
import sphere


class Spheres(object):
    def __init__(self):
        self.spheres = []

        for i in range(1):
            self.spheres.append(sphere.Sphere())

        self.moving = []

        for _ in self.spheres:
            self.moving.append(True)

        self.previous_time = time.time()

    def update(self, box):
        current_time = time.time()
        delta_time = current_time - self.previous_time

        for i, ball in enumerate(self.spheres):
            if self.moving[i]:
                ball.update(delta_time, box)

                self.moving[i] = ball.moving

        self.previous_time = current_time

    def draw(self):
        for ball in self.spheres:
            ball.draw()
