board = [["","",""],["","",""],["","",""]]
player = 1

def checker(x):

    check = 0
    for i in range(3):
        if board[0][i] == x:
            check = check + 1
    if check == 3:
        return 1
    check = 0
    for i in range(3):
        if board[1][i] == x:
            check = check + 1
    if check == 3:
        return 1
    check = 0
    for i in range(3):
        if board[2][i] == x:
            check = check + 1
    if check == 3:
        return 1


    check = 0
    for i in range(3):
        if board[i][0] == x:
            check = check + 1
    if check == 3:
        return 1
    check = 0
    for i in range(3):
        if board[i][1] == x:
            check = check + 1
    if check == 3:
        return 1
    check = 0
    for i in range(3):
        if board[i][2] == x:
            check = check + 1
    if check == 3:
        return 1

    check = 0
    for i in range(3):
        if board[i][i] == x:
            check = check + 1
    if check == 3:
        return 1
    check = 0
    p = 2
    for i in range(3):
        if board[i][p] == x:
            check = check + 1
            p = p - 1
    if check == 3:
        return 1

def move(x, y, player):
    x = x - 1
    y = y - 1
    if board[x][y] == "X" or board[x][y] == "O":
        print("This place is already filled! Opponents turn!")
    else:
        board[x][y] = player

def writeboard():
    for t in board:
        print(t)

def is_filled():
    filled = 0
    for r in range(3):
        for j in range(3):
            if board[r][j] == "O" or board[r][j] == "X":
                filled = filled + 1

    if filled == 9:
        print("It's a tie!")
        return 1

    return 0

while True:
    if player == 1:
        writeboard()
        col = int(input("O! Write a column you want to choose(1-3): "))
        row = int(input("O! Write a row you want to choose(1-3): "))
        if (col >= 1 & col <= 3) & (row >= 1 & row <= 3):
            move(col, row, "O")
            if checker("O") == 1:
                writeboard()
                print("O IS A WINNER!")
                break
            if is_filled() == 1:
                writeboard()
                break
            player = 0
        else:
            print("Out of range! Opponents turn!")
            player = 0
    elif player == 0:
        writeboard()
        col = int(input("X! Write a column you want to choose(1-3): "))
        row = int(input("X! Write a row you want to choose(1-3): "))
        if (col >= 1 & col <= 3) & (row >= 1 & row <= 3):
            move(col, row, "X")
            if checker("X") == 1:
                writeboard()
                print("X IS A WINNER!")
                break
            if is_filled() == 1:
                writeboard()
                break
            player = 1
        else:
            print("Out of range! Opponents turn!")
            player = 1
