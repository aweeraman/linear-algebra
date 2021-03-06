from math import sqrt, acos, degrees, pi

class Vector(object):

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError

            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def add(self, v):
        return [x + y for x, y in zip(self.coordinates, v.coordinates)]

    def minus(self, v):
        return [x - y for x, y in zip(self.coordinates, v.coordinates)]

    def scalar_multiply(self, c):
        return [x * c for x in self.coordinates]

    def magnitude(self):
        return sqrt(sum([x * x for x in self.coordinates]))

    def normalize(self):
        try:
            magnitude = self.magnitude()
            return self.scalar_multiply(1./magnitude)

        except ZeroDivisionError:
            raise Exception('Cannot normalize a zero vector')

    def dot(self, v):
        return sum([x * y for x, y in zip(self.coordinates, v.coordinates)])

    def angle(self, v, deg=False):
        dot = self.dot(v)
        denom = self.magnitude() * v.magnitude()

        if denom == 0.0:
            raise Exception('Cannot calculate angle with zero vector')

        rad = acos(dot/denom)

        if deg:
            return degrees(rad)

        return rad

    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance

    def is_parallel_to(self, v, tolerance=1e-10):
        return ((self.magnitude() < tolerance) or
                (v.magnitude() < tolerance) or
                (self.angle(v) == 0) or
                (self.angle(v) == pi))
