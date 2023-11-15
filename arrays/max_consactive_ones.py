# find the maximum consicetive ones in an array.

arr = [1,1,0,0,1,1,1,0]

def max_consactivez_ones(arr):
    count = 0
    maxi = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
        else:
            count = 0
        maxi = max(maxi, count)
    return maxi

print(max_consactivez_ones(arr))

