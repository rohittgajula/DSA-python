# bubble sort

# itiration 1
# array = [90,3,6,2,1,7,6,5]
#           ^ ^                     swap
#          [3,90,6,2,1,7,6,5]
#              ^ ^                  swap
#          [3,6,90,2,1,7,6,5]
#                ^ ^                swap
#          [3,6,2,90,1,7,6,5]
#                  ^ ^              swap
#          [3,6,2,1,90,7,6,5]
#                    ^ ^            swap
#          [3,6,2,1,7,90,6,5]
#                      ^ ^          swap
#          [3,6,2,1,7,6,90,5]
#                        ^ ^        swap
#          [3,6,2,1,7,6,5,90] #

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

array = [90,3,6,2,1,7,6,5]
print(bubble_sort(array))
