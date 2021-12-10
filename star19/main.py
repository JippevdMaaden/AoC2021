def parse_input(filename):
    lines = []
    with open(filename, "r") as f:
        for readline in f:
            lines.append(readline.split()[0])

    return lines


def find_corrupted_lines(lines):
    # Keep count of every chunk pair
    chunk_open_chars = {"(": ")", "[": "]", "{": "}", "<": ">"}
    chunk_close_chars = {")": 3, "]": 57, "}": 1197, ">": 25137}

    expected_closing_chars_stack = []
    syntax_error_score = 0
    for line in lines:
        for char in line:
            if char in chunk_open_chars.keys():
                expected_closing_chars_stack.append(chunk_open_chars[char])
            elif char in chunk_close_chars.keys():
                expected_char = expected_closing_chars_stack.pop(-1)
                if char != expected_char:
                    # Error
                    syntax_error_score += chunk_close_chars[char]
                    break

    return syntax_error_score


def main():
    lines = parse_input("input.txt")

    syntax_error_score = find_corrupted_lines(lines)
    print(syntax_error_score)


main()
