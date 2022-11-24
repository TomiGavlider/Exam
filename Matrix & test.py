def text_from_matrix(list):
    evenodd = 0
    output = ""
    for line in list:
        if evenodd % 2 == 0:
            evenodd2 = 0
            for even in line:
                if evenodd2 % 2 == 0:
                    output += even
                else:
                    pass
                evenodd2 += 1

        else:
            evenodd2 = 0
            for odd in line:
                if evenodd2 % 2 != 0:
                    output += odd
                else:
                    pass
                evenodd2 += 1

        evenodd += 1
    return output


import unittest


class Testsum(unittest.TestCase):

    def test_method(self):
        self.assertEqual(text_from_matrix([["n", "x"], ["m", "o"]]), "no")

    def test_method2(self):
        self.assertEqual(text_from_matrix([["h", "p", "e"], ["k", "l", "a"], ["l", "m", "o"]]), "hello")


if __name__ == '__main__':
    unittest.main()


