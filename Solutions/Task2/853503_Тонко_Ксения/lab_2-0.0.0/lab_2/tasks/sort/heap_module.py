class Heap:

    def __init__(self):
        self.heap_list = []
        self.file_num_list = []

    def __len__(self):
        return len(self.heap_list)

    def swap(self, i, j):
        self.heap_list[i], self.heap_list[j] = self.heap_list[j], self.heap_list[i]
        self.file_num_list[i], self.file_num_list[j] = self.file_num_list[j], self.file_num_list[i]

    def add_item(self, item, file_num):
        self.heap_list.append(item)
        self.file_num_list.append(file_num)
        current = len(self) - 1
        parent = (current - 1) // 2
        while parent >= 0 and self.heap_list[current] < self.heap_list[parent]:
            self.swap(current, parent)
            current = parent
            parent = (current - 1) // 2

    def down(self, current):
        while current < len(self):
            left_child = current * 2 + 1
            right_child = left_child + 1
            min_child = current
            if left_child < len(self) and self.heap_list[left_child] < self.heap_list[min_child]:
                min_child = left_child
            if right_child < len(self) and self.heap_list[right_child] < self.heap_list[min_child]:
                min_child = right_child
            if min_child == current:
                break
            self.swap(current, min_child)
            current = min_child

    def get_min(self):
        if len(self) == 0:
            return -1, -1
        min_num = self.heap_list[0]
        file_num = self.file_num_list[0]
        self.swap(0, -1)
        self.heap_list.pop()
        self.file_num_list.pop()
        self.down(0)
        return min_num, file_num
