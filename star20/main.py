def parse_input(filename):
    lines = []
    with open(filename, "r") as f:
        for readline in f:
            lines.append(readline.split()[0])

    return lines


def filter_out_corrupted_lines(lines):
    # Keep count of every chunk pair
    chunk_open_chars = {"(": ")", "[": "]", "{": "}", "<": ">"}
    chunk_close_chars = {")": 3, "]": 57, "}": 1197, ">": 25137}

    incomplete_lines = {}
    for line in lines:
        error = False
        expected_closing_chars_stack = []
        for char in line:
            if char in chunk_open_chars.keys():
                expected_closing_chars_stack.append(chunk_open_chars[char])
            elif char in chunk_close_chars.keys():
                expected_char = expected_closing_chars_stack.pop(-1)
                if char != expected_char:
                    # Error
                    error = True

        if not error:
            # If we encountered no error we have an incomplete line
            incomplete_lines[line] = tuple(expected_closing_chars_stack)

    return incomplete_lines


def calculate_autocomplete_scores(incomplete_lines_dict):
    char_value_dict = {")": 1, "]": 2, "}": 3, ">": 4}

    score_list = []
    for incomplete_chars in incomplete_lines_dict.values():
        score = 0
        for char in reversed(incomplete_chars):
            score *= 5
            score += char_value_dict[char]

        score_list.append(score)

    return score_list


def main():
    lines = parse_input("input.txt")

    incomplete_lines_dict = filter_out_corrupted_lines(lines)

    autocomplete_scores_list = calculate_autocomplete_scores(incomplete_lines_dict)
    autocomplete_scores_list.sort()

    print(autocomplete_scores_list[len(autocomplete_scores_list)//2])


main()
