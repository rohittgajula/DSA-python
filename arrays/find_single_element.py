# find the element thats occuring once in an array

arr = [1,1,2,2,3,3,4]

def find_single_element(arr):
    n = len(arr)

    for i in range(n):
        num = arr[i]
        count = 0
        for j in range(n):
            if arr[j] == num:
                count += 1
        if count == 1:
            return num

print(find_single_element(arr))

