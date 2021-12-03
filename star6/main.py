def most_common(char_occurence):
    most_common_char = ""
    if char_occurence >= 0:
        most_common_char = "1"
    elif char_occurence < 0:
        most_common_char = "0"

    return most_common_char


def least_common(char_occurence):
    least_common_char = ""
    if char_occurence >= 0:
        least_common_char = "0"
    elif char_occurence < 0:
        least_common_char = "1"

    return least_common_char


def solve(input_list, index, eval_func):
    # Find common sign for the given index
    char_occurence = 0
    for input in input_list:
        index_char = input[index]
        if index_char == "0":
            char_occurence -= 1
        elif index_char == "1":
            char_occurence += 1

    # Get character to evaluate against
    eval_char = eval_func(char_occurence)

    # Find all corresponding inputs
    correct_input_list = []
    for input in input_list:
        if input[index] == eval_char:
            correct_input_list.append(input)

    # Continue recursion or break if condition is met
    if len(correct_input_list) == 1:
        return correct_input_list[0]
    else:
        return solve(correct_input_list, index + 1, eval_func)


with open("input.txt", "r") as f:
    binary_input_list = []
    for readline in f:
        binary_input_list.append(readline.strip())

    print(int(solve(binary_input_list, 0, most_common), 2) * int(solve(binary_input_list, 0, least_common), 2))
