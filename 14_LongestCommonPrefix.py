

# ==========  LeetCoad 14. Longest Common Prefix

''' =====   Write a function to find the longest common prefix string amongst an array of strings.

            If there is no common prefix, return an empty string "".
'''

''' Example 1:

        Input: strs = ["flower","flow","flight"]
        Output: "fl"
Example 2:

        Input: strs = ["dog","racecar","car"]
        Output: ""
        Explanation: There is no common prefix among the input strings.
 '''
 
 
def bruteforce(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for i in range(len(prefix)):
        for word in strs[1:]:
            if i >= len(word) or word[i] != prefix[i] :
                return prefix[:i]
    return prefix
        
        
def optimal(strs):
    strs.sort()
    first = strs[0]
    last = strs[-1]
    i = 0
    while i < len(first) and first[i] == last[i]:
        i += 1
    return first[:i]


strs = ["Pavan","Pavani","Pallavi"]
print(optimal(strs))
 