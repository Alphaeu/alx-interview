#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.
    
    Args:
    grid (list of list of int): 2D list representing the grid.
    
    Returns:
    int: Perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check the up side
                if r == 0 or grid[r-1][c] == 0:
                    perimeter += 1
                # Check the down side
                if r == rows - 1 or grid[r+1][c] == 0:
                    perimeter += 1
                # Check the left side
                if c == 0 or grid[r][c-1] == 0:
                    perimeter += 1
                # Check the right side
                if c == cols - 1 or grid[r][c+1] == 0:
                    perimeter += 1
    
    return perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))  # Expected output: 12

