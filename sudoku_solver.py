# 'SUDOKU' SOLVER PROGRAM
print("Welcome to Sudoku Game, Have Fun!!")
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


# print board
def print_board(bo):
    for row in range(len(bo)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - -")
        for col in range(len(bo[0])):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")
            if col == 8:
                print(bo[row][col])
            else:
                print(str(bo[row][col]) + " ", end="")
    return None


# pick blank box
def find_empty(bo):
    for row in range(len(bo)):
        for col in range(len(bo[0])):
            if bo[row][col] == 0:
                return (row, col)
    return None


# check for valid board
def valid(bo, num, pos):
    # check horizontally | row
    for h_item in range(len(bo[0])):
        if bo[pos[0]][h_item] == num and pos[1] != h_item:
            return False

    # check vertically | column
    for v_item in range(len(bo)):
        if bo[v_item][pos[1]] == num and pos[0] != v_item:
            return False

    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for row in range(box_y * 3, box_y * 3 + 3):
        for col in range(box_x * 3, box_x * 3 + 3):
            if bo[row][col] == num and (row, col) != pos:
                return False
    return True


# write algorithm to solve
def solve(bo):
    # use recursion
    find = find_empty(bo)
    if not find:
        return True
    else:
        pos = find

    # fill valid value
    for num in range(1, 10):
        if valid(bo, num, pos):
            bo[pos[0]][pos[1]] = num

            if solve(bo):
                return True

            bo[pos[0]][pos[1]] = 0

    return False


print("Board Before")
print(print_board(board))
solve(board)
print("Board After")
print(print_board(board))
