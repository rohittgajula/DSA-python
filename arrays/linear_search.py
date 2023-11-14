arr = [6,5,7,2,3,1,9,0,19]
num = 19
n = len(arr)

# bruteforce solution
def solution(arr, num, n):

    for i in range(n):
        if num not in arr:
            return -1
        elif arr[i] == num:
            return i
        
# optimal solution
def solution1(arr, num, n):
    for index, element in enumerate(arr):
        if element == num:
            return index
    return -1

print(solution(arr, num, n))
print(solution1(arr, num, n))

