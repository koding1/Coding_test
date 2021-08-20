# 1. 도착지점까지의 거리 distance는 1 이상 1,000,000,000 이하입니다. 라는 조건에서 이분탐색 문제임을 떠올리기
# 2. 바위 위치를 sort (오름차순)
# 3. 범위 (s는 0, e는 distance)
# 4. 답(최소값 중 최대값)이 mid라고 가정한다. 
# 5. 돌과 돌 사이를 비교해서 mid 보다 작다면 mid가 최소가 될 수 없으므로, 해당 돌이 제거되었다고 생각하고 제거한다. 
# 6. 제거된 돌의 수를 count하여 n보다 크다면 답이 mid가 되기 위해서는 count 만큼의 돌을 제거야하 함을 의미한다.
# 따라서 mid는 작아져야 한다. (왼쪽으로 탐색)

def solution(distance, rocks, n):
    answer = 0
    
    # 2
    rocks.append(0)
    rocks.append(distance)
    rocks.sort()

    # 3
    s = 0
    e = distance
    
    while s <= e:
        prev = 0
        tmp = -1
        
        # 4
        mid = (s + e) // 2
        
        count = 0
        for i in range(1, len(rocks)):
            
            # 5
            if mid > (rocks[i] - prev) and rocks[i] != distance:
                if mid == 41:
                    print(rocks[i])
                count += 1
            elif mid > (rocks[i] - prev) and rocks[i] == distance:
                if mid == 41:
                    print("도착", rocks[i] - prev)
                tmp = rocks[i] - prev
            elif mid < (rocks[i] - prev):
                prev = rocks[i]
            else: # mid와 일치하는 거리가 있다면
                prev = rocks[i]
                tmp = mid
        # 6
        if count > n:
            print("mid :", mid)
            print("count : ", count)
            print("왼쪽으로 진행")
            e = mid - 1
        elif count < n:
            print("mid :", mid)
            print("count : ", count)
            print("1 오른쪽으로 진행")
            s = mid + 1
        else:
            if tmp != -1 and mid == tmp:
                answer = mid
            print("mid :", mid)
            print("count : ", count)
            print("2 오른쪽으로 진행")
            s = mid + 1
            
    return answer
    
print(solution(42, [10, 20, 30, 40, 41], 1))

# 이건 돼

import math

def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    left, right = 0, distance
    
    answer = 0
    while left <= right:
        prev = 0
        mins = float('inf')

        removed_rocks = 0
        
        mid = (left + right) // 2
        for i in range(len(rocks)):
            if rocks[i] - prev < mid:
                removed_rocks += 1
            else:
                mins = min(mins, rocks[i] - prev)
                prev = rocks[i]
                
        if removed_rocks > n:
            right = mid - 1
        else:
            answer = mins
            left = mid + 1
    return answer
    
print(solution(42, [10, 20, 30, 40, 41], 1))

답이 2가 되야 한다.
