

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

def Optimal_way(matrix):
    max_row,max_sum = max(enumerate(map(sum,matrix)), key = lambda x:x[1])
    print("max_sum", max_sum)
    print("max_row",max_row)

rows = int(input("Enter the length of rows :"))

matrix = [list(map(int,input().split())) for _ in range(rows)]                     # ===== this input is take a matrix in optimal way
print("Highest sum of row in matrix : ", Optimal_way(matrix))