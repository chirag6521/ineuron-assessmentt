# Answer 1

matrix = [[10, 9, 7, 6],
    [5, 4, 3, 2],
    [1, 0, -1, -2]]

def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1

    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1

    return False

# Example :

matrix = [
    [10, 9, 7, 6],
    [5, 4, 3, 2],
    [1, 0, -1, -2]
]
target = 0
print(searchMatrix(matrix, target))  # Output: True
