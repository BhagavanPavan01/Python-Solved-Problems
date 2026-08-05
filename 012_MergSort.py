def merge(left, right, depth):
    print("  " * depth + f"Merging {left} and {right}")

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    print("  " * depth + f"Result -> {result}")
    return result


def merge_sort(arr, depth=0):
    print("  " * depth + f"Divide: {arr}")

    if len(arr) <= 1:
        print("  " * depth + f"Return: {arr}")
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid], depth + 1)
    right = merge_sort(arr[mid:], depth + 1)

    return merge(left, right, depth)


arr = [4, 3, 5, 1, 2]

print("\nFinal Sorted Array:", merge_sort(arr))