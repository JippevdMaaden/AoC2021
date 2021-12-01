with open("input.txt", "r") as f:
    integer_value_list = []
    for line in f.readlines():
        integer_value_list.append(int(line))

    bigger_than_counter = 0
    for index, value in enumerate(integer_value_list):
        next_index = index + 1
        if next_index >= len(integer_value_list):
            pass
        else:
            next_value = integer_value_list[next_index]
            if next_value > value:
                bigger_than_counter += 1

    print(bigger_than_counter)
