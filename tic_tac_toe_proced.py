import os

ROWS = 3
COLS = 3
EMPTY_SYMBOL = "."

board = [[EMPTY_SYMBOL for n in range(COLS)] for m in range(ROWS)]

X_SYMBOL = "X"
O_SYMBOL = "O"

is_X_turn = True


def reset_board():
    _board = [[EMPTY_SYMBOL for n in range(COLS)] for m in range(ROWS)]


def is_board_full():
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == EMPTY_SYMBOL:
                return False
    return True


def print_logo():
    print("┏━┏━━━━━━━━━━━━━┓━┓")
    print("┣━┫ tic tac toe ┣━┫")
    print("┗━┗━━━━━━━━━━━━━┛━┛")


def print_board(x_wins: int, o_wins: int):
    counter = 0
    current_symbol = X_SYMBOL if is_X_turn else O_SYMBOL
    print_logo()
    for i in range(ROWS):
        for j in range(COLS):
            print(board[i][j], end=" ")
        print(end="\t")
        for j in range(COLS):
            counter += 1
            print(counter, end=" ")
        if i == 0:
            print(f"\tX wins: {x_wins}")
        elif i == 1:
            print(f"\tO wins: {o_wins}")
        elif i == 2:
            print(f"\tNow   : {current_symbol}")


def getCellCoordsByNumber(number):
    if number not in range(1, 9 + 1):
        return None

    a = int(number / 3)
    b = int(number % 3)

    if b == 0:
        return a - 1, 2
    else:
        return a, b - 1


def turn():
    global is_X_turn
    isValidInput = False
    while not isValidInput:
        user_input = input("Choose cell[1-9]: ")
        if not user_input.isalnum() or len(user_input) != 1:
            print("Please choose number between 1 and 9")
            continue
        cell_coords = getCellCoordsByNumber(int(user_input))
        if board[cell_coords[0]][cell_coords[1]] != EMPTY_SYMBOL:
            print("This cell is already taken")
            continue

        # if we get to this line then the input is correct
        isValidInput = True
        board[cell_coords[0]][cell_coords[1]] = X_SYMBOL if is_X_turn else O_SYMBOL
        is_X_turn = not is_X_turn  # flipping turn to another player
    return


def isWin():
    # horizontal check
    for i in range(ROWS):
        if board[i][0] == EMPTY_SYMBOL:
            continue
        if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            return board[i][0]  # return the winning symbol
    # vertical check
    for i in range(COLS):
        if board[0][i] == EMPTY_SYMBOL:
            continue
        if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            return board[i][0]  # return the winning symbol
    # diagonals
    if (
        board[0][0] != EMPTY_SYMBOL
        and board[0][0] == board[1][1]
        and board[0][0] == board[2][2]
    ):
        return board[0][0]  # return the winning symbol
    if (
        board[0][2] != EMPTY_SYMBOL
        and board[0][2] == board[1][1]
        and board[0][2] == board[2][0]
    ):
        return board[0][2]  # return the winning symbol

    return EMPTY_SYMBOL


def play_pvp(wins: int = 3):
    """wins parameter is how many wins should one player get untill the game ends, if wins in > 1, then game will start with different symbol making the first turn"""
    global is_X_turn
    x_wins = 0
    o_wins = 0

    isGameOn = True

    while isGameOn:
        os.system("cls")
        print_board(x_wins, o_wins)
        turn()
        winner = isWin()
        if winner != EMPTY_SYMBOL:
            if winner == X_SYMBOL:
                x_wins += 1
            elif winner == O_SYMBOL:
                o_wins += 1
            os.system("cls")
            print_board(x_wins, o_wins)
            print(f"!!!{winner} IS A WINNER!!!")
            is_X_turn = (
                o_wins + x_wins
            ) % 2 == 0  # every win startinf symbol will change

            if o_wins >= wins or x_wins >= wins:
                print(f"!!!{winner} IS AN UNDISPUTED CHAMPION!!!")
                isGameOn = False

            input("press enter...")
            reset_board()

        elif is_board_full():
            os.system("cls")
            print_board(x_wins, o_wins)
            print(f"!!!TIE!!!")
            input("press enter...")
            reset_board()


if __name__ == "__main__":
    play_pvp()
