N = int(input())

numbers = []
for i in range(N):
    numbers.append(int(input()))

# 1. sorted 함수 사용
for i in sorted(numbers):
    print(i)

# 2. merge sort (병합 정렬)
def merge_sort(array):
    
    if len(array) == 1:
        return array

    
    mid = (0 + len(array)) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    
    i = 0
    j = 0
    k = 0
    
    while True:
        if left[i] <= right[j]:
            array[k] = left[i]
            k += 1
            i += 1
        else:
            array[k] = right[j]
            k += 1
            j += 1
        
        if i >= len(left):
            array[k] = right[j]
            break
        if j >= len(right):
            array[k] = left[i]
            break
    
    return tmp
for i in merge_sort(numbers):
    print(i)
