from homework14 import Matrix, MyExceptionMultMatrix, MyExceptionAddMatrix

import unittest


class TestMatrix(unittest.TestCase):

    def setUp(self):
        self.m1 = Matrix([[1, 2], [3, 4]])
        self.m2 = Matrix([[1, 2], [3, 4]])
        self.m3 = Matrix([[1, 2], [3, 4], [5, 6]])

    def test_eq(self):
        self.assertTrue(self.m1 == self.m2, msg="Матрицы не равны")

    def test_add(self):
        self.assertEqual(self.m1 + self.m2, Matrix([[2, 4], [6, 8]]))

    def test_mult(self):
        self.assertEqual(self.m1 * self.m2, Matrix([[7, 10], [15, 22]]))

    def test_add_size_matrix(self):
        with self.assertRaises(MyExceptionAddMatrix):
            self.m1 + self.m3

    def test_mult_size_matrix(self):
        with self.assertRaises(MyExceptionMultMatrix):
            self.m1 * self.m3


if __name__ == '__main__':
    unittest.main()
