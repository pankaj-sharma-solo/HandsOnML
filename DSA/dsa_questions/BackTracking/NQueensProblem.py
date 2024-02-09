def is_safe(board, row, column, n):

    for i in range(column):
        # print(row,",", i, ": ", board[row][i])
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        # print(i,j)
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def print_solution(board, n):
    # print(board)
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

    print()


def solveNQueenUtil(board, col, n):
    # print(board)
    if col >= n:
        print_solution(board, n)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            solveNQueenUtil(board, col+1, n)

            # print(i, " ", col)
            board[i][col] = 0

    return False

def solveNQueen(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solveNQueenUtil(board, 0, n):
        print("solution doesn't exist")
    # else:
    #     print_solution(board, n)

if __name__ == '__main__':
    solveNQueen(4)