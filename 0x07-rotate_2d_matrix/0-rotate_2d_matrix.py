#!/usr/bin/python3
def rotate_2d_matrix(matrix):
    """
    Rotate a n x n 2D matrix 90 degrees clockwise in place.
    
    Args:
    matrix (list of list of int): 2D matrix to rotate
    
    Returns:
    None
    """
    n = len(matrix)
    
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()

# Test the function
if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

