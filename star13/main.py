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


def align_crabs(crab_dict, min_value, max_value):
    fuel_cost_dict = {}
    for i in range(min_value, max_value + 1):
        total_fuel_cost = 0
        for crab_distance, crab_count in crab_dict.items():
            travel_distance = crab_distance - i
            fuel_cost = travel_distance * crab_count
            total_fuel_cost += abs(fuel_cost)

        fuel_cost_dict[i] = total_fuel_cost

    return fuel_cost_dict


def main():
    crab_dict = parse_input("input.txt")
    max_value = max(crab_dict.keys())
    min_value = min(crab_dict.keys())

    fuel_cost_dict = align_crabs(crab_dict, min_value, max_value)

    lowest_fuel_cost = None
    for level, fuel_cost in fuel_cost_dict.items():
        if lowest_fuel_cost:
            if lowest_fuel_cost > fuel_cost:
                lowest_fuel_cost = fuel_cost
        else:
            lowest_fuel_cost = fuel_cost

    print(lowest_fuel_cost)


main()
