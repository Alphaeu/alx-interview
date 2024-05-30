#!/usr/bin/python3
import sys

def is_valid(board, row, col):
    """ Check if a queen can be placed on board[row][col]. """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, N, solutions):
    """ Use backtracking to find all solutions. """
    if row == N:
        solutions.append(board[:])
        return
    
    for col in range(N):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, N, solutions)
            # No need to undo the assignment (board[row] = col), as it will be overwritten

def print_solutions(solutions, N):
    """ Print the solutions in the required format. """
    for solution in solutions:
        formatted_solution = []
        for row in range(N):
            formatted_solution.append([row, solution[row]])
        print(formatted_solution)

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [-1] * N  # This will hold the column positions of queens
    solutions = []
    solve_nqueens(board, 0, N, solutions)
    print_solutions(solutions, N)

if __name__ == "__main__":
    main()

