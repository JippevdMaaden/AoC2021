with open("input.txt", "r") as f:
    bit_position_occurence_dict = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
    }

    for binary_string in f.readlines():
        for index, str_number in enumerate(binary_string):
            try:
                int_number = int(str_number)
            except ValueError:
                continue

            if int_number == 0:
                bit_position_occurence_dict[index] -= 1
            elif int_number == 1:
                bit_position_occurence_dict[index] += 1

    # The value for each key of the bit_position_occurence_dict tells us the
    # occurence of 0's and 1's for each position. A positive number means
    # there are more 1's. A negative number means there are more 0's.

    gamma_rate_str = ""
    epsilon_rate_str = ""
    for i in range(0, 12):
        value = bit_position_occurence_dict[i]
        if value > 0:
            gamma_rate_str += "1"
            epsilon_rate_str += "0"
        elif value < 0:
            gamma_rate_str += "0"
            epsilon_rate_str += "1"

    gamma_rate = int(gamma_rate_str, 2)
    epsilon_rate = int(epsilon_rate_str, 2)

    power_consumption = gamma_rate * epsilon_rate
    print(power_consumption)
