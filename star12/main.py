def parse_input(filename):
    lines_list = []
    with open(filename, "r") as f:
        for readline in f:
            lines_list = list(map(int, readline.split(",")))

    item_dict = {}
    for item in lines_list:
        item_count = item_dict.get(item, 0)
        item_dict[item] = item_count + 1

    return item_dict


def grow_lanternfish(lanternfish_dict, days):
    new_lanternfish_dict = {}
    for lanternfish, count in lanternfish_dict.items():
        new_lanternfish = lanternfish - 1
        if lanternfish == 0:
            # Reset the current lanternfish
            lanternfish_6_count = new_lanternfish_dict.get(6, 0)
            new_lanternfish_dict[6] = lanternfish_6_count + count

            # Add a new lanternfish
            lanternfish_8_count = new_lanternfish_dict.get(8, 0)
            new_lanternfish_dict[8] = lanternfish_8_count + count

        else:
            lanternfish_x_count = new_lanternfish_dict.get(new_lanternfish, 0)
            new_lanternfish_dict[new_lanternfish] = lanternfish_x_count + count

    if days == 0:
        return new_lanternfish_dict
    else:
        return grow_lanternfish(new_lanternfish_dict, days-1)


def main():
    lanternfish_dict = parse_input("input.txt")

    lanternfish_dict_after_256_days = grow_lanternfish(lanternfish_dict, 255)

    total_count = 0
    for lanternfish_count in lanternfish_dict_after_256_days.values():
        total_count += lanternfish_count

    print(total_count)

main()
