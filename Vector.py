from math import sqrt

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
