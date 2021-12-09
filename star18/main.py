INPUT_WIDTH = 100
INPUT_HEIGHT = 100


def parse_input(filename):
    area = []
    with open(filename, "r") as f:
        for readline in f:
            area_line = [int(char) for char in readline.split()[0]]
            area.append(area_line)

    return area


def find_low_points(area):
    low_points = []
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

            if point < min(ajdacent_points):
                low_points.append((i, j))

    return low_points


def get_adjacent_nodes(node):
    adjacency_list = []
    x, y = node
    x_left, x_right = x - 1, x + 1
    y_down, y_up = y - 1, y + 1

    if x_left >= 0:
        # Add left node
        adjacency_list.append((x_left, y))

    if x_right < INPUT_HEIGHT:
        # Add right node
        adjacency_list.append((x_right, y))

    if y_down >= 0:
        # Add down node
        adjacency_list.append((x, y_down))

    if y_up < INPUT_WIDTH:
        # Add up node
        adjacency_list.append((x, y_up))

    return adjacency_list


def get_depth(area, point):
    x, y = point
    return area[x][y]


def find_basin(point, area, basin_points):
    if point not in basin_points:
        # Set up initial conditions
        point_depth = get_depth(area, point)
        adjacency_list = get_adjacent_nodes(point)

        # Since we passed the checke we know we are part of the basin
        basin_points.add(point)

        # Lets see if our neighbours are part of the basin
        for adjacent_point in adjacency_list:
            adjacent_point_depth = get_depth(area, adjacent_point)

            # Only if we go up or stay level are we still in the same basin
            # With a max of 9, since we know these are the peaks.
            if 9 > adjacent_point_depth >= point_depth:
                basin_points = find_basin(adjacent_point, area, basin_points)

            else:
                pass

    return basin_points


def main():
    area = parse_input("input.txt")

    low_points = find_low_points(area)

    basins = []
    for point in low_points:
        basin = find_basin(point, area, set())
        basins.append(len(basin))

    answer = 1
    three_biggest_basins = sorted(basins, reverse=True)[:3]
    for x in three_biggest_basins:
        answer *= x
    print(answer)


main()
