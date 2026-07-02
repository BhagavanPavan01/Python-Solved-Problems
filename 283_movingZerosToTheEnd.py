
# ===================== Leet code Moving zeros to the end ==========
# 
'''Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements. 
   Note that you must do this in-place without making a copy of the array.'''
   
'''Example 1:
   
   Input: nums = [0,1,0,3,12]
   Output: [1,3,12,0,0]
   
   Example 2:
   
   Input: nums = [0]
   Output: [0]'''

# this is optimal way of code complexity is O(n) ====================

def ZerosMoveToEnd(n):
    pointer = 0
    for i in range(len(n)):
        if n[i] != 0:
            n[pointer],n[i] = n[i],n[pointer]
            pointer += 1
    return n

#  this is Brute force way ========================================

def BruteZerosMoveToEnd(n):
    non_zeros = n.count(0)
    
    while 0 in nums:
        n.remove(0)
    for _ in range(non_zeros):
        n.append(0)
    return n


nums = list(map(int, input("Enter the array elements : ").split()))

print(BruteZerosMoveToEnd(nums))