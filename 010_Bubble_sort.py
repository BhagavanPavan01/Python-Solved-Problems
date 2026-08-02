

# ==================== Bubble sort algorithm ======================

def Bubble_sort_brute(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:        # just change ">" to "<" it sort using decending order
                arr[j],arr[j+1] = arr[j+1],arr[j]
                print(arr)
    return arr


def Bubble_sort_optimal(arr,k):
    n = len(arr)
    for i in range(n):
        flag = False
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:           # just change ">" to "<" it sort using decending order
                arr[j],arr[j+1] = arr[j+1],arr[j]
                print(arr)
            flag = True
            
        if not flag:
            break
    return arr[-k]
    
    
    
    
    
    
arr = [3,5,7,9,4,0,1,2,3,4,5]
k = 2
# print(Bubble_sort_brute(arr))
print(Bubble_sort_optimal(arr,k))