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

my1 = Matrix(4, 4)
my2 = Matrix(4, 1)

my1.set(1, 1, 1)
my2.set(1, 1, 4)

my3 = my1.times(my2)
