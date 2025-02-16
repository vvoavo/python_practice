import os

BOARD_WIDTH = 7
BOARD_HEIGHT = 6

board = [["." for n in range(0, BOARD_WIDTH)] for i in range(0, BOARD_HEIGHT)]


def printBoard():
    for i in range(BOARD_HEIGHT):
        print("| ", end="")
        for j in range(BOARD_WIDTH):
            print(board[i][j] + " ", end="")
        print("|")
    # print("[===============]")
    print("[=1=2=3=4=5=6=7=]")


def dropCoin(coin_symbol, column):
    for j in range(BOARD_WIDTH):
        if board[BOARD_HEIGHT - j - 1][column] == ".":
            board[BOARD_HEIGHT - j - 1][column] = coin_symbol
            return True
    return False  # returns false in case of bein unable to find empty cell (when column is full)


def checkWinHorizontal():
    for i in range(BOARD_HEIGHT):
        for j in range(BOARD_WIDTH - 3):
            if board[i][j] == ".":
                continue
            if (
                board[i][j] == board[i][j + 1]
                and board[i][j] == board[i][j + 2]
                and board[i][j] == board[i][j + 3]
            ):
                return board[i][j]
    return "."


def checkWinVertical():
    for i in range(BOARD_HEIGHT - 3):
        for j in range(BOARD_WIDTH):
            if board[i][j] == ".":
                continue
            if (
                board[i][j] == board[i + 1][j]
                and board[i][j] == board[i + 2][j]
                and board[i][j] == board[i + 3][j]
            ):
                return board[i][j]
    return "."


def checkWinDiagonal():
    for i in range(BOARD_HEIGHT - 3):
        for j in range(BOARD_WIDTH - 3):
            if board[i][j] == ".":
                continue
            if (
                board[i][j] == board[i + 1][j + 1]
                and board[i][j] == board[i + 2][j + 2]
                and board[i][j] == board[i + 3][j + 3]
            ):
                return board[i][j]

    for i in range(BOARD_HEIGHT - 3):
        for j in range(BOARD_WIDTH - 3):
            if board[i][BOARD_WIDTH - j - 1] == ".":
                continue
            if (
                board[i][BOARD_WIDTH - j - 1] == board[i + 1][BOARD_WIDTH - j - 2]
                and board[i][BOARD_WIDTH - j - 1] == board[i + 2][BOARD_WIDTH - j - 3]
                and board[i][BOARD_WIDTH - j - 1] == board[i + 3][BOARD_WIDTH - j - 4]
            ):
                return board[i][BOARD_WIDTH - j - 1]
    return "."


def checkWin():
    h = checkWinHorizontal()
    v = checkWinVertical()
    d = checkWinDiagonal()
    if h != ".":
        return h
    elif v != ".":
        return v
    elif d != ".":
        return d
    return "."


def getColumnInput():

    isValidInput = False

    column_input = "0"

    while not isValidInput:
        column_input = input("\nEnter column to drop:")

        if not column_input.isalnum():
            print("\nEnter number from 1 to 7\n")
            continue

        column_input = int(column_input)

        if column_input not in range(1, 7):
            print("\nEnter number from 1 to 7\n")
            continue

        isValidInput = True

    return column_input


def play_pvp():
    p1 = "."
    p2 = "."
    os.system("cls")
    while True:
        p1 = input("Choose symbol for player 1: ")
        if len(p1) > 1:
            print("Enter ONE symbol")
        elif p1 == ".":
            print("Enter diffenter symbol")
        else:
            break
    os.system("cls")
    while True:
        p2 = input("Choose symbol for player 2: ")
        if len(p2) > 1:
            print("Enter ONE symbol")
        elif p2 == p1 or p2 == ".":
            print("Enter diffenter symbol")
        else:
            break

    isGameOn = True
    isP1Turn = True
    while isGameOn:
        os.system("cls")

        currentCoin = p1 if isP1Turn else p2
        print(f"     {p1} VS {p2}")
        print(f"now dropping: {currentCoin}\n")
        printBoard()
        column_input = getColumnInput()

        if dropCoin(currentCoin, column_input - 1):
            winner = checkWin()
            if winner != ".":
                os.system("cls")

                print(f"\n     {p1} VS {p2}")
                printBoard()
                print(f"\n ################")
                print(f"#### {currentCoin} WINS ####")
                print(f"################")
                isGameOn = False

            isP1Turn = not isP1Turn


play_pvp()
