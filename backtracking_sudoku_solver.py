board = [
    [8, 6, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 7, 0, 0, 0, 5, 9],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 6, 0, 8, 0, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 5, 3, 0, 0, 0, 0, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 6, 0, 0],
    [0, 0, 7, 5, 0, 9, 0, 0, 0]
]

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("------------------------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty_position(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None

def is_Valid(board, position, number):
    #check row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False

    #check column
    for i in range(len(board[0])):
        if board[i][position[1]] == number and position[0] != i:
            return False

    #check cube
    cube_x = position[1] // 3
    cube_y = position[0] // 3

    for i in range(cube_y * 3, cube_y * 3 + 3):
        for j in range(cube_x * 3, cube_x * 3 + 3):
            if board[i][j] == number and (i,j) != position:
                return False

    return True

def solve_board(board):
    print_board(board)
    print("------------------------")
    empty_position = find_empty_position(board)

    #base case
    if not empty_position:
        return True
    else:
        row, col = empty_position

    for i in range(1, 10):
        if is_Valid(board, (row, col), i):
            board[row][col] = i

            #backtrack and try again
            if solve_board(board):
                return True
            board[row][col] = 0

    return False


print_board(board)
solve_board(board)
print("___________________________")
print("SOLVED!")
print_board(board)



