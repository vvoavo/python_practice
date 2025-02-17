import os


class TicTacToe(object):
    def __init__(self):
        self._ROWS = 3
        self._COLS = 3
        self._EMPTY_SYMBOL = "."

        self._board = [
            [self._EMPTY_SYMBOL for n in range(self._COLS)] for m in range(self._ROWS)
        ]

        self._X_SYMBOL = "X"
        self._O_SYMBOL = "O"

        self._is_X_turn = True

    def _reset_board(self):
        self._board = [
            [self._EMPTY_SYMBOL for n in range(self._COLS)] for m in range(self._ROWS)
        ]

    def _is_board_full(self):
        for i in range(self._ROWS):
            for j in range(self._COLS):
                if self._board[i][j] == self._EMPTY_SYMBOL:
                    return False
        return True

    def _print_logo(self):
        print("┏━┏━━━━━━━━━━━━━┓━┓")
        print("┣━┫ tic tac toe ┣━┫")
        print("┗━┗━━━━━━━━━━━━━┛━┛")

    def _print_board(self, x_wins: int, o_wins: int):
        counter = 0
        current_symbol = self._X_SYMBOL if self._is_X_turn else self._O_SYMBOL
        self._print_logo()
        for i in range(self._ROWS):
            for j in range(self._COLS):
                print(self._board[i][j], end=" ")
            print(end="\t")
            for j in range(self._COLS):
                counter += 1
                print(counter, end=" ")
            if i == 0:
                print(f"\tX wins: {x_wins}")
            elif i == 1:
                print(f"\tO wins: {o_wins}")
            elif i == 2:
                print(f"\tNow   : {current_symbol}")

    def _getCellCoordsByNumber(self, number):
        if number not in range(1, 9 + 1):
            return None

        a = int(number / 3)
        b = int(number % 3)

        if b == 0:
            return a - 1, 2
        else:
            return a, b - 1

    def _turn(self):
        isValidInput = False
        while not isValidInput:
            user_input = input("Choose cell[1-9]: ")
            if not user_input.isalnum() or len(user_input) != 1:
                print("Please choose number between 1 and 9")
                continue
            cell_coords = self._getCellCoordsByNumber(int(user_input))
            if self._board[cell_coords[0]][cell_coords[1]] != self._EMPTY_SYMBOL:
                print("This cell is already taken")
                continue

            # if we get to this line then the input is correct
            isValidInput = True
            self._board[cell_coords[0]][cell_coords[1]] = (
                self._X_SYMBOL if self._is_X_turn else self._O_SYMBOL
            )
            self._is_X_turn = not self._is_X_turn  # flipping turn to another player
        return

    def _isWin(self):
        # horizontal check
        for i in range(self._ROWS):
            if self._board[i][0] == self._EMPTY_SYMBOL:
                continue
            if (
                self._board[i][0] == self._board[i][1]
                and self._board[i][0] == self._board[i][2]
            ):
                return self._board[i][0]  # return the winning symbol
        # vertical check
        for i in range(self._COLS):
            if self._board[0][i] == self._EMPTY_SYMBOL:
                continue
            if (
                self._board[0][i] == self._board[1][i]
                and self._board[0][i] == self._board[2][i]
            ):
                return self._board[i][0]  # return the winning symbol
        # diagonals
        if (
            self._board[0][0] != self._EMPTY_SYMBOL
            and self._board[0][0] == self._board[1][1]
            and self._board[0][0] == self._board[2][2]
        ):
            return self._board[0][0]  # return the winning symbol
        if (
            self._board[0][2] != self._EMPTY_SYMBOL
            and self._board[0][2] == self._board[1][1]
            and self._board[0][2] == self._board[2][0]
        ):
            return self._board[0][2]  # return the winning symbol

        return self._EMPTY_SYMBOL

    def play_pvp(self, wins: int = 3):
        """wins parameter is how many wins should one player get untill the game ends, if wins in > 1, then game will start with different symbol making the first turn"""
        x_wins = 0
        o_wins = 0

        isGameOn = True

        while isGameOn:
            os.system("cls")
            self._print_board(x_wins, o_wins)
            self._turn()
            winner = self._isWin()
            if winner != self._EMPTY_SYMBOL:
                if winner == self._X_SYMBOL:
                    x_wins += 1
                elif winner == self._O_SYMBOL:
                    o_wins += 1
                os.system("cls")
                self._print_board(x_wins, o_wins)
                print(f"!!!{winner} IS A WINNER!!!")
                self._is_X_turn = (
                    o_wins + x_wins
                ) % 2 == 0  # every win startinf symbol will change

                if o_wins >= wins or x_wins >= wins:
                    print(f"!!!{winner} IS AN UNDISPUTED CHAMPION!!!")
                    isGameOn = False

                input("press enter...")
                self._reset_board()

            elif self._is_board_full():
                os.system("cls")
                self._print_board(x_wins, o_wins)
                print(f"!!!TIE!!!")
                input("press enter...")
                self._reset_board()


game = TicTacToe()
game.play_pvp()
