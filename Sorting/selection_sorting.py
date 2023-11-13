# sort the given array in to non-decending order using selection sorting method

# arr = [5,4,3,2,1]

#       [5,4,3,2,1]
#        ^ ^        4 < 5

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        minIndexValue = i
        for j in range(i+1, n):
            if arr[j] < arr[minIndexValue]:
                minIndexValue = j
                print(arr)
        temp = arr[i]
        arr[i] = arr[minIndexValue]
        arr[minIndexValue] = temp
        print(arr)
        print()
    return arr

arr = [5,4,3,2,1]
print(selection_sort(arr))
