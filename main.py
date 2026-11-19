import numpy as np

board = np.array([
    list(map(int, input().strip())) for _ in range(9)
])

def get_board():
    pass

def check_row(board, row, num):
    for i in board[row]:
        if i==num:
            return False
    return True

def check_column(board, col, num):
    for i in board[: , col]:
        if i==num:
            return False
    return True

def check_grid(board, row, col, num):
    row_start = (row//3)*3
    col_start = (col//3)*3

    grid = board[row_start:row_start+3, col_start:col_start+3]
    for i in grid.ravel():
        if i==num:
            return False
    return True

def display_board(board):
    print("    1 2 3   4 5 6   7 8 9")
    print("  +-------+-------+-------+")

    for i in range(9):
        print(f"{i} |", end=" ")

        for j in range(9):
            print(int(board[i][j]), end=" ")

            if (j + 1) % 3 == 0 and j != 8:
                print("|", end=" ")

        print("|")

        if (i + 1) % 3 == 0:
            print("  +-------+-------+-------+")


def solve(board):
    empty_row=0
    empty_col=0
    for i in range(0,9):
        for j in range(0,9):
            if board[i][j]==0:
                empty_row=i
                empty_col=j

                for i in range(1,10):
                    A = check_row(board,empty_row,i)
                    B = check_column(board,empty_col,i)
                    C = check_grid(board,empty_row,empty_col,i)

                    if A & B & C:
                        board[empty_row][empty_col] = i
                        if solve(board):
                            return True
                        board[empty_row][empty_col] = 0
                return False
    return True

solve(board)
display_board(board)
