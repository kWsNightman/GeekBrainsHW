class Matrix:
    count = 1

    def __init__(self, matrix):
        self.matrix = matrix
        self.count = Matrix.count
        Matrix.count += 1

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))

    def __add__(self, other):
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[i]))] for i in
                       range(len(self.matrix))])


m_1_1 = Matrix([[32, 123], [123, 432], [45, 65]])
m_1_2 = Matrix([[1, 23], [23, 43], [78, 12]])
print(f'Matrix {m_1_1.count}: \n {m_1_1}')
print(f'Matrix {m_1_2.count}: \n {m_1_2}')
print(f'Summ matrix {m_1_1.count} and {m_1_2.count}: \n{m_1_1 + m_1_2}')
m_2_1 = Matrix([[3, 12, 1], [13, 32, 12], [3, 1, 4]])
m_2_2 = Matrix([[87, 65, 0], [54, 38, 95], [12, 6, 0]])
print(f'Matrix {m_2_1.count}: \n {m_2_1}')
print(f'Matrix {m_2_2.count}: \n {m_2_2}')
print(f'Summ matrix {m_2_1.count} and {m_2_2.count}: \n{m_2_1 + m_2_2}')
m_3_1 = Matrix([[3, 12, 1, 4], [13, 32, 12, 6]])
m_3_2 = Matrix([[87, 65, 0, 9], [54, 38, 95, 54]])
print(f'Matrix {m_3_1.count}: \n {m_3_1}')
print(f'Matrix {m_3_2.count}: \n {m_3_2}')
print(f'Summ matrix {m_3_1.count} and {m_3_2.count}: \n{m_3_1 + m_3_2}')
