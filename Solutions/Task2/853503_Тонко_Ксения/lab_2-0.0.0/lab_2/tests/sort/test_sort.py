import unittest
import lab_2.tasks.sort.task_1_sort as sort
import random


class TestSort(unittest.TestCase):

    def test(self):
        in_file = 'numbers.txt'
        out_file = 'sorted.txt'

        def create_files(count):
            with open(in_file, 'w') as file:
                file.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(count))
            sort.merge_sort(in_file, out_file)

        def check_sort(count):
            create_files(count)
            count, prev_num = 0, 0
            with open(out_file, 'r') as file:
                for line in file:
                    cur_num = int(line)
                    if count > 0:
                        self.assertTrue(prev_num <= cur_num)
                    else:
                        count += 1
                    prev_num = cur_num

        check_sort(10)
        check_sort(1000)
        check_sort(1000000)
