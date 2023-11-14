# write the union of two arrays in a sorted order.

a = [1,2,3,5,6]
b = [2,4,5,7]
n = len(a)
m = len(b)

# uning unions method in set
def solution(a,b,n,m):
    union = set(a).union(set(b))
    result = list(union)
    return result

# without using union
def solution1(a,b,n,m):
    union_set = set()
    result = []
    for i in a:
        union_set.add(i)
    for j in b:
        union_set.add(j)
    result = list(union_set)
    result.sort()
    return result

print(solution(a,b,n,m))
print(solution1(a,b,n,m))
