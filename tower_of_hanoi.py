DISK_AMOUNT = 5
TOWER_HEIGHT = DISK_AMOUNT + 1
SOLVED_COL = [(DISK_AMOUNT) - n for n in range(TOWER_HEIGHT)]

col_1 = [(DISK_AMOUNT) - n for n in range(TOWER_HEIGHT)]
col_2 = [0 for n in range(TOWER_HEIGHT)]
col_3 = [0 for n in range(TOWER_HEIGHT)]


def canBeMoved(col_from, col_to):
    if col_from[0] == 0:
        return False

    disk_to_move = 0
    disk_to_land = 0

    for i in range(1, len(col_from)):
        if col_from[i] == 0:
            disk_to_move = col_from[i - 1]
            break
    for i in range(1, len(col_to)):
        if col_to[i] == 0:
            disk_to_land = col_to[i - 1]
            break

    return disk_to_land == 0 or disk_to_land > disk_to_move


def moveDisk(col_from, col_to):
    if not canBeMoved(col_from, col_to):
        return False

    disk_to_move_id = 0
    disk_to_land_id = 0

    for i in range(1, len(col_from)):
        if col_from[i] == 0:
            disk_to_move_id = i - 1
            break

    for i in range(0, len(col_to)):
        if col_to[i] == 0:
            disk_to_land_id = i
            break

    col_to[disk_to_land_id] = col_from[disk_to_move_id]
    col_from[disk_to_move_id] = 0
    return True


# TODO make print look like actual disks of different sizes
def printTowers():
    disks_str = [
        "    |    ",
        "    1    ",
        "   [2]   ",
        "  [#3#]  ",
        " [##4##] ",
        "[###5###]",
    ]
    for i in range(0, TOWER_HEIGHT):
        print(
            f"\t{disks_str[col_1[TOWER_HEIGHT-1-i]]}\t{disks_str[col_2[TOWER_HEIGHT-1-i]]}\t{disks_str[col_3[TOWER_HEIGHT-1-i]]}"
        )
    print("\n\t    1\t\t    2\t\t    3")
    return


def playerInput():
    isValidFromInput = False
    isValidToInput = False
    from_id = 0
    to_id = 0
    while not isValidFromInput:
        from_id = input("Choose tower to take disk from: ")
        if from_id.isalnum():
            from_id = int(from_id)
        else:
            print("invalid input")

        if from_id in range(1, 3 + 1):
            isValidFromInput = True
        else:
            print("please choose correct option")

    while not isValidToInput:
        to_id = input("Choose tower to put disk on to: ")

        if to_id.isalnum():
            to_id = int(to_id)
        else:
            print("invalid input")

        if to_id in range(1, 3 + 1) and to_id != from_id:
            isValidToInput = True
        else:
            print("please choose correct option")
    return from_id, to_id


def colFromId(tower_id):
    match tower_id:
        case 1:
            return col_1
        case 2:
            return col_2
        case 3:
            return col_3
        case _:
            return False


def towerOfHanoi():

    isGameSolved = False
    while not isGameSolved:
        printTowers()
        input = playerInput()
        col_from = colFromId(input[0])
        print(col_from)
        col_to = colFromId(input[1])
        print(col_to)
        if not moveDisk(col_from, col_to):
            print("failed to move disk")


towerOfHanoi()
