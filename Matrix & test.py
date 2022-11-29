def text_from_matrix(list):
    even = 0
    odd = 0
    output = ""
    for line in list:
        if even% 2 == 0:
            even = 0
            for even in line:
                if even % 2 == 0:
                    output += even
                else:
                    pass
                odd += 1

        else:
            odd = 0
            for odd in line:
                if odd % 2 != 0:
                    output += odd
                else:
                    pass
                odd += 1

        odd += 1
    return output


import unittest


class Testsum(unittest.TestCase):

    def test_method(self):
        self.assertEqual(text_from_matrix([["n", "x"], ["m", "o"]]), "no")

    def test_method2(self):
        self.assertEqual(text_from_matrix([["h", "p", "e"], ["k", "l", "a"], ["l", "m", "o"]]), "hello")


if __name__ == '__main__':
    unittest.main()


