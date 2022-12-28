

def transpose_matrix(matrix):
    list = []
    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    for r in result:
        list.append(r)
    return list


import unittest


class Testsum(unittest.TestCase):

    def test_method1(self):
        expected_output = [[1, 4], [2, 5], [3, 6]]
        result = transpose_matrix([[1,2,3],[4,5,6]])

        self.assertEqual(result,expected_output)

    def test_method2(self):
        expected_output = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        result = transpose_matrix([[1,2,3],[4,5,6],[7,8,9]])

        self.assertEqual(result, expected_output)



if __name__ == 'main':
    unittest.main()
