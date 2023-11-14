# rotate an given array by one step to the left.

arr = [2,3,4,5]

# this is the bruteforce solution.
def rotate(arr, n):
    temp = [0] * n
    for i in range(1,n):
        temp[i-1] = arr[i]
    temp[n-1] = arr[0]

    for i in range(n):
        print(temp[i], end=" ")
    print()

# optimal solution
def solution(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp

    for i in range(n):
        print(arr[i], end=" ")
    print()

print(f'given array : {arr}')
rotate(arr, len(arr))
solution(arr, len(arr))
