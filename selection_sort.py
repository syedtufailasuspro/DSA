def selection_sort(arr):
    a = arr[:]  # Create a copy so original list is not modified
    n = len(a)
    swaps = 0

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        # Only swap if needed
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1

    print("Sorted Array:", a)
    print("Total Swaps:", swaps)
    return a

selection_sort([1,54,5,5,48,4,654,6])