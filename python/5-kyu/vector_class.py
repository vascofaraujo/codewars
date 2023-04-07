class Vector:
  # TODO: Finish the Vector class.
    def __init__(self, *args):
        vector = []
        len_vector = 0
        for arg in args[0]:
            vector.append(arg)
            len_vector += 1
        self.vector = vector
        self.vector_len = len_vector

    def __str__(self):
        out = '('
        for idx, i in enumerate(self.vector):
            if idx != 0:
                out += ','
            out += str(i)
        out += ')'
        return out

    def equals(self, x):
        if not self.vector_len==x.vector_len:
            return False
        for a, b in zip(self.vector, x.vector):
            if a != b:
                return False
        return True

    def add(self, x):
        if not self.vector_len==x.vector_len:
            raise Exception()
        new_vector = []
        for a, b in zip(self.vector, x.vector):
            new_vector.append(a+b)
        return Vector(new_vector)

    def subtract(self, x):
        if not self.vector_len==x.vector_len:
            raise Exception()
        new_vector = []
        for a, b in zip(self.vector, x.vector):
            new_vector.append(a-b)
        return Vector(new_vector)

    def dot(self, x):
        if not self.vector_len==x.vector_len:
            raise Exception()
        new_vector = []
        out = 0
        for a, b in zip(self.vector, x.vector):
            out += (a*b)
        return out

    def norm(self):
        norm = 0
        for a in self.vector:
            norm += a**2
        return norm**(1/2)


if __name__=='__main__':
    a = Vector([1, 2, 3])
    b = Vector([3, 4, 5])
    c = Vector([5, 6, 7, 8])

    print(a.add(b))      # should return a new Vector([4, 6, 8])
    print(a.subtract(b)) # should return a new Vector([-2, -2, -2])
    print(a.dot(b))      # should return 1*3 + 2*4 + 3*5 = 26
    print(a.norm())      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
    print(a.add(c))      # raises an exception
