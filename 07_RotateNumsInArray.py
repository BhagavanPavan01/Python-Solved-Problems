

#  ===========================  Rotate the Numbers in Array =================

def rotation(s,k):
    k = len(s)
    for i in range(k // 2):
        s[i], s[k-1] = s[k-1], s[i]
        k = k-i
    return s



arr = list(map(int, input("Enter the array : ").split()))
k = int(input())
print(rotation(arr,k))
