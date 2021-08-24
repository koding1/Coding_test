N = int(input())
N_list = list(map(int, input().split(' ')))
M = int(input())
M_list = list(map(int, input().split(' ')))

# 이진 탐색을 위한 정렬
N_list.sort()

for i in M_list:
    s = 0
    e = N-1
    check = 0
    while s <= e:
        mid = (s + e) // 2
        # -> 으로 진행
        if N_list[mid] < i:
            s = mid + 1
        # <- 으로 진행
        elif N_list[mid] > i:
            e = mid - 1
        else:
            check = 1
            break
    print(check)
