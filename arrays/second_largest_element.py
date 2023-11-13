# find the second largest and second smallest element in an array.

arr = [5,6,4,7,8,8,8,9]
n = len(arr)

def element(arr, n):
    largest = float('-inf')
    second_largest = float('-inf')
    smallest = float('inf')
    second_smallest = float('inf')

    for i in range(n):
        smallest = min(smallest, arr[i])
        largest = max(largest, arr[i])

    for i in range(n):
        if arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]
        if arr[i] < second_smallest and arr[i] != smallest:
            second_smallest = arr[i]
    return second_smallest, second_largest

def largest_smallest(arr, n):
    largest = float('-inf')
    smallest = float('inf')

    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest, largest

print(element(arr, n))
print(largest_smallest(arr, n))

