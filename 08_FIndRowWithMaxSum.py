

# =================== Find The row with max sum ================================

def FindRowWithMaxSum (matrix):
    max_sum = float("-inf")
    max_index = -1
    
    for row in matrix :
        row_sum = sum(row)
        if row_sum > max_sum :
            max_sum = row_sum
            max_index = row
    return max_sum and max_index


rows = int(input("Enter the length of rows :"))

matrix = [list(map(int,input().split())) for _ in range(rows)]                     # ===== this input is take a matrix in optimal way
print("Highest sum of row in matrix : ", FindRowWithMaxSum(matrix))