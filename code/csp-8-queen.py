# install following dependencies:
# pip install python-constraint

# 8-Queens Problem

import constraint as cst


def display_chessboard(board):
    print('  A B C D E F G H')

    for i in range(8):
        print(i + 1, end=' ')
        for j in range(8):
            print(board[i][j], end=' ')
        print("")

        
def fill_chessboard(board, col, row):
    board[col][row] = '■' # placing the queen in the right cell
    return board


def print_solutions(solutions):
    counter = 0
    
    for solution in solutions:
        counter += 1
        chess_board = [["□" for x in range(8)] for y in range(8)] # creating an empty chessboard
        print(f"Solution #{counter}")
        print(solution)
        print("")

        for key in solution:
            chess_board = fill_chessboard(chess_board, key - 1, solution[key] - 1)

        display_chessboard(chess_board)
        print("")


def main():
    problem = cst.Problem()

    cols = range(1,9)
    rows = range(1,9)

    problem.addVariables(cols, rows)

    for col1 in cols:
        for col2 in cols:
            if col1 < col2:
                problem.addConstraint(lambda row1, row2, col1=col1, col2=col2:
                                     row1 != row2 # checking they are not in the same row
                                      and abs(col1 - col2) != abs(row1 - row2), # checking diagonally
                                     (col1, col2))


    solutions = problem.getSolutions()

    print(f"Total number of solutions: {len(solutions)}")
    print("")

    print_solutions(solutions)

    
if __name__ == "__main__":
    main()
