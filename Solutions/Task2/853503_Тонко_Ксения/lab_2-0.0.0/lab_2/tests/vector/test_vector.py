import unittest
import lab_2.tasks.vector.task_3_vector as vct


class TestVector(unittest.TestCase):

    def setUp(self):
        self.vect_1 = vct.Vector(1, 2, 3)
        self.vect_2 = vct.Vector(3, 7, 10)
        self.vect_3 = vct.Vector(2.1, 5.2, 4.7)

    def test_init(self):
        self.assertEqual(len(self.vect_1), 3)
        self.assertEqual(self.vect_1.type, int)
        self.assertEqual(self.vect_3.type, float)
        self.assertEqual(self.vect_1.items, [1, 2, 3])

    def test_add(self):
        result = self.vect_1 + self.vect_2
        answer = vct.Vector(4, 9, 13)
        self.assertEqual(result, answer)
        self.assertEqual(result.type, int)
        result = self.vect_1 + self.vect_3
        answer = vct.Vector(3.1, 7.2, 7.7)
        self.assertEqual(result, answer)
        self.assertEqual(result.type, float)

    def test_sub_vector(self):
        result = self.vect_1 - self.vect_2
        answer = vct.Vector(-2, -5, -7)
        self.assertEqual(result, answer)

    def test_mul_vector(self):
        result = self.vect_1 * self.vect_2
        self.assertEqual(result, 47)

    def test_mul_const(self):
        result = self.vect_1 * 3
        answer = vct.Vector(3, 6, 9)
        self.assertEqual(result, answer)
        self.assertEqual(result.type, int)
        result = self.vect_3 * 2
        answer = vct.Vector(4.2, 10.4, 9.4)
        self.assertEqual(result, answer)
        self.assertEqual(result.type, float)
