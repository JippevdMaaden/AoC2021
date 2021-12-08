def parse_input(filename):
    input_list = []
    output_list = []
    with open(filename, "r") as f:
        for readline in f:
            # clean_readline = readline.split()
            # print(clean_readline)
            output, input = readline.split("|")
            input_list.append(input.split())
            output_list.append(output.split())

    return input_list, output_list

def count_output_digits(output_list):
    digit_count_dict = {}
    for output in output_list:
        for value in output:
            number_of_digits = len(value)
            current_value_count = digit_count_dict.get(number_of_digits, 0)
            digit_count_dict[number_of_digits] = current_value_count + 1

    return digit_count_dict


def main():
    output_list, input_list = parse_input("input.txt")
    digit_count_dict = count_output_digits(output_list)

    number_of_1_4_7_and_8 = 0
    for digits, count in digit_count_dict.items():
        if digits in [2, 3, 4, 7]:
            number_of_1_4_7_and_8 += count
    print(number_of_1_4_7_and_8)

main()
