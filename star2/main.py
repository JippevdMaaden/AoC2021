with open("input.txt", "r") as f:
    integer_value_list = []
    for line in f.readlines():
        integer_value_list.append(int(line))

    bigger_than_counter = 0
    for index, value in enumerate(integer_value_list):
        first_next_index = index + 1
        second_next_index = index + 2
        third_next_index = index + 3

        if third_next_index >= len(integer_value_list):
            pass
        else:
            current_window = value + integer_value_list[first_next_index] + integer_value_list[second_next_index]
            next_window = integer_value_list[first_next_index] + integer_value_list[second_next_index] + integer_value_list[third_next_index]

            if next_window > current_window:
                bigger_than_counter += 1

    print(bigger_than_counter)
