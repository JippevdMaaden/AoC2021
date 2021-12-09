def parse_input(filename):
    area = []
    with open(filename, "r") as f:
        for readline in f:
            area_line = [int(char) for char in readline.split()[0]]
            area.append(area_line)

    return area


def find_low_point_score(area):
    total_score = 0
    for i, area_line in enumerate(area):
        try:
            if i > 0:
                previous_area_line = area[i-1]
            else:
                previous_area_line = []
        except IndexError:
            previous_area_line = []

        try:
            next_area_line = area[i+1]
        except IndexError:
            next_area_line = []

        for j, point in enumerate(area_line):
            ajdacent_points = []
            try:
                if j > 0:  # Else we get the last point again from the row
                    ajdacent_points.append(area_line[j-1])
            except IndexError:
                # No point to the left
                pass

            try:
                ajdacent_points.append(area_line[j+1])
            except IndexError:
                # No point to the right
                pass

            if previous_area_line:
                ajdacent_points.append(previous_area_line[j])

            if next_area_line:
                ajdacent_points.append(next_area_line[j])

            # print("check")
            # print(point)
            # print(len(ajdacent_points))
            # print(ajdacent_points)
            if point < min(ajdacent_points):
                # print(f"point {point} is the low point out of {ajdacent_points}")
                risk_level = point + 1
                total_score += risk_level

    return total_score


def main():
    area = parse_input("input.txt")
    print(area)

    low_points_score = find_low_point_score(area)
    print(low_points_score)


main()
