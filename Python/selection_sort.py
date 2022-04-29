def selection_sort(arr):
    for i in range(len(arr)-1):
        minpos = i
        for j in range(i,len(arr)):
            if arr[j]< arr[minpos]:
                minpos = j

        arr[i], arr[minpos] = arr[minpos], arr[i]

        # print(arr)
arr = [5,3,8,6,7,2]
selection_sort(arr)
print(arr)
