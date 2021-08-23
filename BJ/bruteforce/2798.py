from collections import deque

N, M = map(int, input().split(' '))

numbers = [int(num) for num in input().split(' ')]

max_ = 0

for i in range(0, N):
    s1 = numbers[i]
    for j in range(i + 1, N):
        if i != j:
            s2 = numbers[j]
        for k in range(j + 1, N):
            if i != j != k:
                s3 = numbers[k]
        
            if (s1 + s2 + s3 <= M) and (max_ < s1 + s2 + s3):
                max_ = s1 + s2 + s3
            
print(max_)
