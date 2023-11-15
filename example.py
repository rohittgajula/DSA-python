nums = [1,1,0,0,1,1,1]

def consective_ones(nums):
    count = 0
    maxi = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            count = 0
        maxi = max(maxi, count)
    return maxi

print(consective_ones(nums))

