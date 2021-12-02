with open("input.txt", "r") as f:
    total_command_dict = {
        "forward": 0,
        "down": 0,
        "up": 0,
    }
    for line in f.readlines():
        # Split command str and int value
        command_list = line.split(" ")
        command_direction = command_list[0]
        command_value = int(command_list[1])

        total_command_dict[command_direction] += command_value

    depth_position = total_command_dict["down"] - total_command_dict["up"]
    horizontal_position = total_command_dict["forward"]

    print(depth_position * horizontal_position)
