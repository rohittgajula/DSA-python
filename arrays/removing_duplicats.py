# remove duplicate from an given array


arr = [3,2,5,5,6,3,9]
n = len(arr)

def remove_duplicates(arr, n):

    result = []
    no = 0
    for i in range(n):
        if arr[i] not in result:
            no += 1
            result.append(arr[i])
    return f"No of non-duplicate elements in an arrat are : {no}, they are {result}"

print(remove_duplicates(arr, n))

