# find the largest element in an given array

def largest_element(arr):
    n = len(arr)
    max=arr[0]
    for i in range(n):
        if arr[i] > max:
            max = arr[i]
    return max


arr = [4,6,3,5,0,1]
print(largest_element(arr))

