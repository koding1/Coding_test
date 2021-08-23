N = int(input())

min_ = N + 1
check = False
for i in range(N):
    current = i + sum([int(j) for j in str(i)])
    if current == N:
        min_ = min(min_, i)
        check = True
if check:        
    print(min_)
else:
    print(0)
