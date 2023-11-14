# in a given array move all the zeros to the end.

arr = [5,7,0,3,5,0,1]
n = len(arr)

# bruteforce solution
def solution(arr, n):
    non_zero = []
    zero = []
    for i in range(n):
        if arr[i] != 0:
            non_zero.append(arr[i])
        if arr[i] == 0:
            zero.append(arr[i])
    return non_zero+zero

# optimal solution
def solution1(arr, n):
    non_zero = []
    count = 0
    for i in arr:
        if i != 0:
            non_zero.append(i)
        else:
            count += 1
    return non_zero + [0] * count


print(solution(arr, n))
print(solution1(arr, n))