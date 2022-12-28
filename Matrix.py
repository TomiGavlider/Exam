

def transpose_matrix(matrix):
    list = []
    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    for r in result:
        list.append(r)
    print(list)

transpose_matrix([[1,2,3],[4,5,6],[7,8,9]])

import unittest


class Testsum(unittest.TestCase):

    def test_method1(self):

        self.assertEqual(transpose_matrix([[1,2,3],[4,5,6]]), None)

    def test_method2(self):

        self.assert_(transpose_matrix([[1,2,3],[4,5,6],[7,8,9]]), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])



if __name__ == 'main':
    unittest.main()
