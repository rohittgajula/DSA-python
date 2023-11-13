arr = [1,2,3,4,5,0]
n = len(arr)

# brute force solution
def isSorted(arr, n):

    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                return False
            
    return True

# optomised solution
def sorted(arr, n):
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            print(i)
            print(f'arr[i] : {arr[i]}')
            print(f'arr[i-1] : {arr[i-1]}')
            print()
            return False
    return True

print(isSorted(arr, n))
print(sorted(arr, n))

