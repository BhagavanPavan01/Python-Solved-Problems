
# ===================== Intersection of two arrays ===============

'''     Given two integer arrays nums1 and nums2, return an array of their intersection. 
    Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.'''


# ========== Brute force way ==================

def brute(nums1,nums2):
    common = []
    for i in nums1:
        for z in nums2:
            if i == z :
                common.append(i)
    return list(set(common))

# ========== medium Brute force way ==================


def mediambrute(nums1,nums2):
    common = []
    m = len(nums1)
    n = len(nums2)
    if m > n :
        for num in nums1:
            if (num in nums2) and (num not in common):
                common.append(num)
    else:
        for num in nums2:
            if (num in nums1) and (num not in common):
                common.append(num)
    return common

# ========== Optimal way ==================

def optimal(nums1,nums2):
    return list(set(nums1) & set(nums2))


arr1 = list(map(int,input("Enter the arr1 : ").split()))
arr2 = list(map(int,input("Enter the arr2 : ").split()))

print(brute(arr1,arr2))
print(mediambrute(arr1,arr2))
print(optimal(arr1,arr2))