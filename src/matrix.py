import itertools

class Matrix(object):
    """A matrix on a certain field."""

    def __init__(self, m, n, entries = None):
        self.m = m
        self.n = n

        if entries == None:
            entries = [[0 for x in range(n)] for y in range(m)]
        self.entries = []
        try:
            assert len(entries) == m, 'entries parameter is of incorrect dimensions'
            for i in range(m):
                assert len(entries[i]) == n, 'entries parameter is of incorrect dimensions'
                self.entries.append([])
                for j in range(n):
                    self.entries[i].append(entries[i][j])
        except Exception as error:
            print(error)

    def get(self, i, j):
        """Returns the i, j entry of self"""
        try:
            return self.entries[i - 1][j - 1]
        except IndexError:
            print("Please use indices within bounds!")


    def set(self, i, j, val):
        """Sets the value of entry i, j to val"""
        try:
            self.entries[i - 1][j - 1] = val
        except IndexError:
            print("Please use indices within bounds!")

    def dimensions(self):
        """Returns the dimensions of this matrix"""
        return self.m, self.n

    def times(self, B):
        """Returns the matrix product of this self and B"""

        assert type(self) == type(B), "Please input a Matrix"
        assert self.dimensions()[1] == B.dimensions()[0], "Please input Matrices of complementary size"

        dot_length = self.dimensions()[1]
        new_m = self.dimensions()[0]
        new_n = B.dimensions()[1]
        return_matrix = Matrix(new_m, new_n)
        for i in range(1, new_m + 1):
            for j in range(1, new_n + 1):
                new_val = sum([self.get(i, k) * B.get(k, j) for k in range(1, dot_length + 1)])
                return_matrix.set(i, j, new_val)

        return return_matrix

    def __mul__(self, other):
        return times(self, other)

    def __add__(self, other):
        dim = self.dimensions()
        new = Matrix(dim[0], dim[1])
        for i in range(1, dim[0] + 1):
            for j in range(1, dim[1] + 1):
                new.set(i, j, self.get(i, j) + other.get(i, j))
        return new

    def __getitem__(self, key):
        return self.get(key[0], key[1])

    def __eq__(self, other):
        if self.dimensions() != other.dimensions():
            return False
        else:
            for i in range(1, self.dimensions()[0] + 1):
                for j in range(1, self.dimensions()[1] + 1):
                    if self[i, j] != other[i, j]:
                        return False
        return True

    def __repr__(self):
        return "\n".join([str(c) for c in self.entries])

    def determinant(self):
        det = 0
        for perm in itertools.permutations(range(1, self.dimensions()[0]  + 1)):
            det += sign(perm) * prod([self.get(perm[i], i + 1) for i in range(self.dimensions()[0])])
        return det

def prod(li):
    n = 1
    for i in li:
        n *= i
    return n

def sign(permutation):
  sign = 1
  n = len(permutation)
  for i in range(n):
    for j in range(i + 1, n):
      if permutation[i] > permutation[j]:
        sign *= -1
  return sign

