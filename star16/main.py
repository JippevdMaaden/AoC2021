def parse_input(filename):
    input_list = []
    output_list = []
    with open(filename, "r") as f:
        for readline in f:
            output, _input = readline.split("|")
            input_list.append(_input.split())
            output_list.append(output.split())

    return input_list, output_list


def count_output_value(input_list, output_list):
    """
    Map to:
     aaaa
    b    c
    b    c
     dddd
    e    f
    e    f
     gggg

    Using the numbers:
      0:      1:      2:      3:      4:
     aaaa    ....    aaaa    aaaa    ....
    b    c  .    c  .    c  .    c  b    c
    b    c  .    c  .    c  .    c  b    c
     ....    ....    dddd    dddd    dddd
    e    f  .    f  e    .  .    f  .    f
    e    f  .    f  e    .  .    f  .    f
     gggg    ....    gggg    gggg    ....

      5:      6:      7:      8:      9:
     aaaa    aaaa    aaaa    aaaa    aaaa
    b    .  b    .  .    c  b    c  b    c
    b    .  b    .  .    c  b    c  b    c
     dddd    dddd    ....    dddd    dddd
    .    f  e    f  .    f  e    f  .    f
    .    f  e    f  .    f  e    f  .    f
     gggg    gggg    ....    gggg    gggg

    total occurences:
    a = 8
    b = 6
    c = 8
    d = 7
    e = 4
    f = 9
    g = 7
    """
    total_sum = 0
    mapping_possibilities = ["a", "b", "c", "d", "e", "f", "g"]
    for i, _input in enumerate(input_list):
        _output = output_list[i]
        mapping_dict = {}
        input_string = "".join(_input)

        number_4_string = next((x for x in _input if len(x) == 4), "")
        number_1_string = next((x for x in _input if len(x) == 2), "")

        # Create mapping dict
        for mapping_char in mapping_possibilities:
            input_char_count = input_string.count(mapping_char)
            mapped_to_char = ""
            if input_char_count == 4:
                mapped_to_char = "e"
            elif input_char_count == 6:
                mapped_to_char = "b"
            elif input_char_count == 7:
                if mapping_char in number_4_string:
                    mapped_to_char = "d"
                else:
                    mapped_to_char = "g"
            elif input_char_count == 8:
                if mapping_char in number_1_string:
                    mapped_to_char = "c"
                else:
                    mapped_to_char = "a"
            elif input_char_count == 9:
                mapped_to_char = "f"

            mapping_dict[mapped_to_char] = mapping_char

        # Use mapping dict and digit length to find the digit
        output_value_string = ""
        for digit in _output:
            if len(digit) == 2:
                output_value_string += "1"
            elif len(digit) == 3:
                output_value_string += "7"
            elif len(digit) == 4:
                output_value_string += "4"
            elif len(digit) == 7:
                output_value_string += "8"
            elif len(digit) == 5:
                # Either 2, 3 or 5
                if mapping_dict["e"] in digit:
                    output_value_string += "2"
                elif mapping_dict["b"] in digit:
                    output_value_string += "5"
                else:
                    output_value_string += "3"
            elif len(digit) == 6:
                # Either 0, 6, 9
                if mapping_dict["c"] not in digit:
                    output_value_string += "6"
                elif mapping_dict["e"] not in digit:
                    output_value_string += "9"
                else:
                    output_value_string += "0"

        # Add the integer digit to the total sum
        total_sum += int(output_value_string)

    return total_sum


def main():
    output_list, input_list = parse_input("input.txt")
    total_sum = count_output_value(input_list, output_list)

    print(total_sum)


main()
