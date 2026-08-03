from typing import List

def rotate(matrix: List[List[int]]) -> None:
    l, r = 0, len(matrix) - 1
    while l < r:
        for i in range(r - l):
            top, bottom = l, r
            # Save the top-left element
            topLeft = matrix[top][l + i]
            # Move bottom-left to top-left
            matrix[top][l + i] = matrix[bottom - i][l]
            # Move bottom-right to bottom-left
            matrix[bottom - i][l] = matrix[bottom][r - i]
            # Move top-right to bottom-right
            matrix[bottom][r - i] = matrix[top + i][r]
            # Move top-left to top-right
            matrix[top + i][r] = topLeft
        l += 1
        r -= 1
        
# Example usage:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(matrix)
print(matrix)  

            