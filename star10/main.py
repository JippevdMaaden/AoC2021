def parse_input(filename):
    lines_list = []
    with open(filename, "r") as f:
        for readline in f:
            point_1_and_2 = readline.split(" -> ")
            x1, y1 = point_1_and_2[0].split(",")
            x2, y2 = point_1_and_2[1].split(",")
            lines_list.append(((int(x1), int(y1)), (int(x2), int(y2))))

    return lines_list


def find_line_coverage(line):
    set_of_covered_points = set()
    x1, y1 = line[0]
    x2, y2 = line[1]

    if x1 == x2:
        # Line is vertical
        for i in range(min((y1, y2)), max((y1, y2))):
            set_of_covered_points.add((x1, i))

    elif y1 == y2:
        # Line is horizontal
        for i in range(min((x1, x2)), max((x1, x2))):
            set_of_covered_points.add((i, y1))

    else:
        # Line is diagonal
        if x1 > x2:
            x1, y1, x2, y2 = x2, y2, x1, y1

        slope = (y2 - y1) // (x2 - x1)
        for i, j in zip(range(x1, x2), range(y1, y2, slope)):
            set_of_covered_points.add((i, j))

    set_of_covered_points.add(line[0])
    set_of_covered_points.add(line[1])

    return set_of_covered_points


def main():
    point_coverage_dict = {}
    lines_list = parse_input("input.txt")
    for line in lines_list:
        line_coverage = find_line_coverage(line)
        for point in line_coverage:
            current_point_coverage_value = point_coverage_dict.get(point, 0)
            new_point_coverage_value = current_point_coverage_value + 1
            point_coverage_dict[point] = new_point_coverage_value

    list_of_points_where_coverage_higher_than_one = []
    for point, coverage in point_coverage_dict.items():
        if coverage > 1:
            list_of_points_where_coverage_higher_than_one.append(point)

    print(len(list_of_points_where_coverage_higher_than_one))


main()
