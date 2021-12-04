class BingoBoard:
    def __init__(self):
        self.board = []
        self.board_marked = []

    def add_new_line(self, line):
        self.board.append(line)
        self.board_marked.append([0 for x in line])

    def has_complete_row(self):
        for line in self.board_marked:
            if sum(line) == 5:
                return True

        return False

    def has_complete_column(self):
        for i in range(0, 5):
            if sum([row[i] for row in self.board_marked]) == 5:
                return True

        return False

    def check_for_win(self):
        return self.has_complete_row() or self.has_complete_column()

    def mark_number(self, string_number):
        for i, line in enumerate(self.board):
            for j in range(0, 5):
                if line[j] == string_number:
                    self.board_marked[i][j] = 1
                    self.board[i][j] = 0

        return self.check_for_win()


def parse_input(filename):
    bingo_input_list = []
    bingo_board_list = []
    new_bingo_board = BingoBoard()
    with open(filename, "r") as f:
        for i, readline in enumerate(f):
            if i == 0:
                # Bingo input line
                bingo_input_list = readline.strip().split(",")

            if i == 1:
                pass

            else:
                bingo_list = readline.split()

                # Bingo board inputs
                if len(bingo_list) == 5:
                    new_bingo_board.add_new_line(bingo_list)
                else:
                    # End current board, start new
                    bingo_board_list.append(new_bingo_board)
                    new_bingo_board = BingoBoard()

        # Append the last bingo board
        bingo_board_list.append(new_bingo_board)

    return bingo_input_list, bingo_board_list


def main():
    bingo_input_list, bingo_board_list = parse_input("input.txt")

    for i, string_number in enumerate(bingo_input_list):
        for bingo_board in bingo_board_list:
            if bingo_board.mark_number(string_number=string_number):
                unmarked_sum = 0
                for line in bingo_board.board:
                    for bingo_tile in line:
                        unmarked_sum += int(bingo_tile)
                print(unmarked_sum * int(string_number))
                quit()

main()
