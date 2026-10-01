

# ================ Back Tracking =======================

# def backtrack(path, nums):
#     if not nums:
#         print(path)
#         return

#     for x in nums:
#         path.append(x)

#         backtrack(path, [n for n in nums if n != x])

#         path.pop()


# backtrack([], [1, 2,() 3, 4, 5])


def printSubsets(index,current,s):
    if index == len(s):
        print(current)
        return
    printSubsets(index + 1, current, s)
    printSubsets(index + 1,current + s[index],s)
    
    
s = "abcd"
printSubsets(0, "", s)
    