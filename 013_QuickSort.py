# =================  Quick Sort ======================

def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    print(left,right,pivot)
    return QuickSort(left) + [pivot] + QuickSort(right)




arr = [2,4,291,22,44,91,6,4,7,10,1,100,1]

print(QuickSort(arr))