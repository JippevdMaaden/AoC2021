with open("input.txt", "r") as f:
    total_command_dict = {
        "forward": 0,
        "depth": 0,
        "aim": 0,
    }
    for line in f.readlines():
        # Split command str and int value
        command_list = line.split(" ")
        command_direction = command_list[0]
        command_value = int(command_list[1])

        if command_direction == "forward":
            total_command_dict[command_direction] += command_value
            total_command_dict["depth"] += total_command_dict["aim"] * command_value
        elif command_direction == "up":
            total_command_dict["aim"] -= command_value
        elif command_direction == "down":
            total_command_dict["aim"] += command_value

    depth_position = total_command_dict["depth"]
    horizontal_position = total_command_dict["forward"]

    print(depth_position * horizontal_position)
