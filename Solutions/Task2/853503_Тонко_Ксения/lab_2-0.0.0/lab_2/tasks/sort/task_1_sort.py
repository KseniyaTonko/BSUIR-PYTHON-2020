import tempfile
import lab_2.tasks.sort.heap_module as hp


def get_temp_files(file_name):
    temp_count = 1000000
    file_names, numbers = [], []
    file_num, count = 0, 0
    with open(file_name) as file:
        for line in file:
            file_num += 1
            if file_num % temp_count == 1:
                if file_num != 1:
                    file_names[-1][1] = count
                    numbers.sort()
                    with open(new_file.name, 'a') as new_file_w:
                        for number in numbers:
                            new_file_w.writelines(str(number) + '\n')
                    numbers.clear()
                new_file = tempfile.NamedTemporaryFile('w+t', delete=False)
                file_names.append([new_file.name, 0])
                new_file.close()
                count = 0
            numbers.append(int(line))
            count += 1
    file_names[-1][1] = count
    numbers.sort()
    with open(new_file.name, 'a') as new_file_w:
        for number in numbers:
            new_file_w.writelines(str(number) + '\n')
    return file_names


def merge_sort(in_file_name, out_file_name):
    file_names = get_temp_files(in_file_name)
    index = [1] * len(file_names)
    out_file = open(out_file_name, 'w')
    out_file.close()
    out_file = open(out_file_name, 'a')
    heap = hp.Heap()

    for i in range(len(file_names)):
        with open(file_names[i][0]) as file:
            line = int(file.readline())
            heap.add_item(line, i)

    files = []
    for item in file_names:
        files.append(open(item[0], 'r'))

    while len(heap) > 0:
        min_num, i = heap.get_min()
        if index[i] < file_names[i][1]:
            line = files[i].readline()
            heap.add_item(int(line), i)
            index[i] += 1
        out_file.writelines(str(min_num) + '\n')

    for file in files:
        file.close()
    tmp = tempfile.TemporaryDirectory()
    tmp.cleanup()
    out_file.close()
