import unittest
import lab_2.tasks.singleton.singleton as sing


class TestSingleton(unittest.TestCase):

    def test(self):

        class Student(metaclass=sing.Singleton):

            def __init__(self, name, rating):
                self.name = name
                self.rating = rating

        student_1 = Student("Andrey", 10)
        student_2 = Student("Katya", 77)
        student_3 = Student()
        self.assertEqual(student_1, student_2)
        self.assertEqual(student_2, student_3)
