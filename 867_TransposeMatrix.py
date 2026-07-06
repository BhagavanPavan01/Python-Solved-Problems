

# ============== Transpose of matrix =========================

'''
            Given a 2D integer array matrix, return the transpose of matrix.
        The transpose of a matrix is the matrix flipped over its main diagonal, 
        switching the matrix's row and column indices.'''
        
        
'''
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
'''

# ==================== Brute force way ============================


def transpose(matrix):
    m = len(matrix)
    n = len(matrix[0])
    result = [[0] * m for _ in range(n)]
    
    for i in range(m):
        for j in range(n):
            result[j][i] = matrix[i][j]
    return result

# ======================== Optimal way ==============================

def optimalTranspose(matrix):
    return [list(row) for row in zip(*matrix)]

# ====================== Take a 2D array as a matrix ==================
# == this is one way
rows = int(input("Enter the length of rows : "))
cols = int(input("Enter the length of cols : "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Enter element[{i}][{j}]"))
        row.append(value)
    matrix.append(row)
    
# ==== this is another way
# rows = int(input())
# cols = int(input())

# matrix = [list(map(int, input().split())) for _ in range(rows)]
# ======================
    
print(matrix) # ==========> this is the actual matrix
    
print(optimalTranspose(matrix))