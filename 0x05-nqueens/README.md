To tackle the N Queens problem using Python, you'll be implementing a solution that employs the backtracking algorithm. Here’s a structured plan to guide you through the process:

### Step-by-Step Implementation

1. **Setup the Project Directory and Files:**
    - Create a directory named `0x05-nqueens`.
    - Inside this directory, create a file named `0-nqueens.py`.
    - Ensure all files are executable and comply with PEP 8 style guide.

2. **Handle Command-Line Arguments:**
    - Your script should take exactly one command-line argument, `N`.
    - Validate the argument to ensure it's an integer greater than or equal to 4.
    - Handle incorrect inputs gracefully by printing appropriate error messages.

3. **Implement the Backtracking Algorithm:**
    - Use recursion to explore all possible placements of queens on the board.
    - Ensure no two queens threaten each other by checking rows, columns, and diagonals.

4. **Print the Solutions:**
    - Format each solution as a list of lists, where each inner list contains two integers representing the row and column of a queen.

Here’s a detailed implementation of the solution:

### Code Implementation

```python
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
```

### Explanation

1. **Command-Line Argument Handling:**
    - Check the number of arguments.
    - Validate that `N` is an integer and at least 4.
    - Print appropriate error messages and exit if the conditions are not met.

2. **Backtracking Algorithm:**
    - `is_valid` function ensures no two queens threaten each other.
    - `solve_nqueens` function places queens on the board row by row using backtracking.
    - Store each valid board configuration in the `solutions` list.

3. **Output:**
    - `print_solutions` function formats and prints each solution as required.

### Running the Program
Make sure to make your script executable:
```bash
chmod +x 0-nqueens.py
```

Execute the program with a valid integer `N`:
```bash
./0-nqueens.py 4
./0-nqueens.py 6
```

This structured approach ensures you handle input validation, implement the core backtracking algorithm, and format the output correctly, providing a complete solution to the N Queens problem.
