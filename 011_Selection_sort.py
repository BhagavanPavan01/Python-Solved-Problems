# ======================== Selection Sort ====================

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr



def Optimal_selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        is_sorted = True
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
                is_sorted = False
        
        if min_index != i:
            arr[i],arr[min_index] = arr[min_index],arr[i]
        if is_sorted:
            break
    return arr
   


arr = [4,6,4,7,8,9,2,32,2,56,0]

print(Optimal_selection_sort(arr))
# print(selection_sort(arr))