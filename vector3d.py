import math


class Vector3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def magnitude(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z))

    def dot(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z

        return math.sqrt((x * x) + (y * y) + (z * z))

    def normalise(self):
        magnitude = self.magnitude()

        if magnitude != 0:
            self.x /= magnitude
            self.y /= magnitude
            self.z /= magnitude
        else:
            self.x = 0
            self.y = 0
            self.z = 0
