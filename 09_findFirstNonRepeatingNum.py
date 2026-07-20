

# ==========  Find the First non reapeting number a array ===========


def brute(arr):
    n = len(arr)
    
    for i in range(n):
        unique = True
        for j in range(n):
            if i !=j and arr[i] == arr[j]:
                unique = False
                break
        if unique:
            return arr[i]
    return -1


#  ============= opimal way =============

def optimal(arr):
    freq = {}
    for i in arr:
        freq[i] = freq.get(i,0) + 1
        
    for i in arr:
        if freq[i] == 1 :
            return i
    return -1



arr = [9,1,9,3,6,3,4,1,6,4]
print(optimal(arr))