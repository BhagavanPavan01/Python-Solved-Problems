
# ==== Hash Map ============

def hashmap(li):
    dici = {}
    n = len(li)
    
    for i in range(n):
        val = li[i]
        if val not in dici:
            dici[val] = 1
        else:
            dici[val] = dici[val] + 1

    return dici




li = [1,2,5,6,4,8,1,2,5,4,8,6,2,5,7,5,2,1,6,5,47,5,2,1,5]
print(hashmap(li))
