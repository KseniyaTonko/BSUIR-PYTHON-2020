import unittest
from lab_2.tasks.cached.task_4_cached import cached


class TestCached(unittest.TestCase):

    def test(self):

        @cached
        def sum(a, b):
            return a + b

        self.assertIs(sum(3, 7), 10)
        self.assertIs(sum(-5, 2), -3)
        self.assertIs(sum(0, 0), 0)
