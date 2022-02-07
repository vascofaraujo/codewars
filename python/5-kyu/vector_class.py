class Vector:
  # TODO: Finish the Vector class.
    def __init__(self, *args):
        vector = []
        len_vector = 0
        for arg in args:
            vector.append(vector)
            len_vector += 1
        self.vector = vector
        self.vector_len = len_vector
                
    def add(self, x):
        assert self.vector_len==x.vector_len
        new_vector = []
        for a, b in zip(self.vector, x.vector):
            new_vector.append(a+b)
        return new_vector
    
    def subtract(self, x):
        assert self.vector_len==x.vector_len
        new_vector = []
        for a, b in zip(self.vector, x.vector):
            new_vector.append(a-b)
        return new_vector
    
    def dot(self, x):
        assert self.vector_len==x.vector_len
        new_vector = []
        for a, b in zip(self.vector, x.vector):
            new_vector.append(a*b)
        return new_vector
    
    def norm(self):
        norm = 0
        for a in self.vector:
            norm += a**(-1/2)
        return norm
