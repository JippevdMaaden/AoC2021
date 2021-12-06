def parse_input(filename):
    lines_list = []
    with open(filename, "r") as f:
        for readline in f:
            lines_list = list(map(int, readline.split(",")))

    return lines_list


def grow_lanternfish(lanternfish_list, days):
    new_lanternfish_list = []
    for lanternfish in lanternfish_list:
        if lanternfish == 0:
            # Reset the current lanternfish
            new_lanternfish_list.append(6)

            # Add a new lanternfish
            new_lanternfish_list.append(8)

        else:
            new_lanternfish_list.append(lanternfish-1)

    if days == 0:
        return new_lanternfish_list
    else:
        return grow_lanternfish(new_lanternfish_list, days-1)


def main():
    lanternfish_list = parse_input("input.txt")

    lanternfish_list_after_80_days = grow_lanternfish(lanternfish_list, 79)
    print(len(lanternfish_list_after_80_days))

main()
