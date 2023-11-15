# find the missing number in a array, using linear search.

nums = [1]

def missing_number(nums):
    n = len(nums) + 1
    for i in range(1, n + 1):       # here n+1 is exclusive
        if i not in nums:
            return i
        
# better approach'
def missing_num(arr):
    N = len(arr)
    hash = [0] * (N + 1)
    for i in range(N-1):
        hash[nums[i]] += 1
    for i in range(1, N+1):
        if hash[i] == 0:
            return i+1

print(missing_num(nums))
print(missing_number(nums))

