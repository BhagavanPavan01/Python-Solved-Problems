
# ============== Leet code problem 74 Search a 2D matrix =================
# 
# Problem====


# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.
 
# example :
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# ==========  normal Brute force approach ================ in normal python

# ======== main class in Brute Force approach ==================

# class Solution(object):
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         for row in matrix:
#             for col in row:
#                 if target == col:
#                     return True
#         return False


#  ============ Binary Search Approach =================

class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = (rows * cols) - 1

        while low <= high :
            mid = (low + high) // 2

            row = mid // cols
            col = mid % cols
            middle_value = matrix[row][col]
            if middle_value == target:
                return True
            elif middle_value < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
        

# Take matrix input ================

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter sorted matrix values row by row:")

for i in range(rows):
    values = list(map(int, input().split()))
    
    if len(values) != cols:
        print("Enter exactly", cols, "values")
        exit()
    
    matrix.append(values)

target = int(input("Enter target value: "))

obj = Solution()
print("Found:", obj.searchMatrix(matrix, target))


    
