class TicTacToe:
    def __init__(self, curr_state):
        self.curr_state: str = curr_state
        self.win_count: int = 0
        self.winner: str = ""
        self.is_possible: bool = True
        self.is_draw: bool = True
        self.game_status: bool = False

    def __repr__(self):
        return "Console game +-+-+-+TicTacToe+-+-+-+: \n" \
               f"Current state: {self.curr_state} \n" \
               f"Count of win: {self.win_count} \n" \
               f"Winner: {self.winner} \n" \
               f"Is possible: {self.is_possible} \n" \
               f"Is draw: {self.is_draw} \n" \
               f"Game status is {int(self.game_status)}"

    def __str__(self):
        return f"TicTacToe(curr_state: {self.curr_state}, " \
               f"win_count: {self.win_count}, " \
               f"winner: {self.winner}, " \
               f"is_possible: {self.is_possible}, " \
               f"is_draw: {self.is_draw}, " \
               f"game_status: {self.game_status})"

    def check_horizontal_win(self):
        for i in range(0, 8, 3):
            if self.curr_state[i:i+3] == "XXX":
                self.winner = "X"
                self.win_count += 1
            elif self.curr_state[i:i+3] == "OOO":
                self.winner = "O"
                self.win_count += 1

    def check_vertical_win(self):
        for i in range(0, 3):
            if self.curr_state[i] + self.curr_state[i + 3] + self.curr_state[i + 6] == "XXX":
                self.winner = "X"
                self.win_count += 1
            elif self.curr_state[i] + self.curr_state[i + 3] + self.curr_state[i + 6] == "OOO":
                self.winner = "O"
                self.win_count += 1

    def check_dioganally_win(self):
        if self.curr_state[0] + self.curr_state[2] + self.curr_state[8] == "XXX" \
                or self.curr_state[2] + self.curr_state[4] + self.curr_state[6] == "XXX":
            self.winner = "X"
            self.win_count += 1
        elif self.curr_state[0] + self.curr_state[2] + self.curr_state[8] == "OOO" \
                or self.curr_state[2] + self.curr_state[4] + self.curr_state[6] == "OOO":
            self.winner = "O"
            self.win_count += 1

    def check_win(self):
        self.check_horizontal_win()
        self.check_vertical_win()
        self.check_dioganally_win()

    def check_possible(self):
        null_count = self.curr_state.count("O")
        x_count = self.curr_state.count("X")

        self.is_possible = self.win_count <= 1 and (null_count == x_count - 1 or x_count == null_count - 1
                                                    or null_count == x_count)

    def check_draw(self):
        empty_count = self.curr_state.count("_")
        self.is_draw = empty_count == 0

    @staticmethod
    def print_border():
        print("---------")

    def print_curr_state(self):
        curr_row = 1
        curr_symbol = 0
        for elem in self.curr_state:
            curr_symbol += 1
            if curr_symbol % 3 == 0:
                print(elem + " ", end="")
                print("|")
                curr_row += 1
            elif (curr_symbol - 1) % 3 == 0:
                print("| ", end="")
            if curr_symbol % 3 > 0:
                print(elem + " ", end="")

    def start(self):
        self.game_status = True
        self.print_border()
        self.print_curr_state()
        self.print_border()
        self.check_win()
        self.check_possible()
        self.check_draw()
        if self.is_possible:
            if self.is_draw and self.win_count == 0:
                print("Draw")
                self.game_status = False
            elif not self.is_draw and self.win_count == 0:
                print("Game not finished")
            else:
                print(f"{self.winner} wins")
                self.game_status = False
        else:
            print("Impossible")
            self.game_status = False


def main():
    cells = input("Enter cells: > ")
    tic_tac_toe = TicTacToe(cells)
    tic_tac_toe.start()


if __name__ == "__main__":
    main()
