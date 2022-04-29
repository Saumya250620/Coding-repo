def quick_sort(sequence):
    l = len(sequence)
    if l <= 1:
        return sequence
    else:
        pivot = sequence.pop()


    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([2,1,8,6,5,7,3,4]))

'''
def quicksort(arr,left,right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left,partition_pos - 1)
        quicksort(arr, partition_pos +1, right)

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i< j:
        while i < right and arr[i] < pivot:
            i += 1

        while j > left and arr[j] >= pivot:
            j-=1

        if i < j:
            arr[i],arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i


arr = [2,1,8,6,5,7,3,4]
quicksort(arr, 0, len(arr)-1)
print(arr)
'''
