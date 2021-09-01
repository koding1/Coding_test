from collections import deque

# 다리가 견디는 최대 트럭 수, 다리가 견디는 무게, 각 트럭의 무게
# 문제 설명 부족 -> 트럭은 1초에 1만큼 움직인다
# 문제 설명 부족 -> 모든 트럭의 길이는 1이다
def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    # truck_weights list를 queue 자료 구조 라고 생각하고 구현
    truck_weights = deque(truck_weights)
    
    seconds = 0
    
    bridge = deque()
    # sum(bridge) : 브릿지에 있는 모든 차의 무게 -> 대신 이 변수를 사용
    now_bridge_weight = 0
    
    while truck_weights:
        current = truck_weights.popleft()
        print(bridge)
        while True:
            if (now_bridge_weight + current < weight) and len(bridge) + 1 <= bridge_length:
                # 무게, 현재 위치에서 다리 끝까지의 거리
                seconds += 1
                
                # 현재 다리 위의 차들이 모두 1씩 전진했다고 생각
                seconds -= len(bridge)
                    
                bridge.append([current, bridge_length])
                now_bridge_weight += current
                break
            else:
                if not (now_bridge_weight + current < weight):
                    tmp = bridge.popleft()
                    
                    seconds += (tmp[1] - 1) # 빠지면서 들어오므로 들어오는 시간 계산
                    now_bridge_weight -= tmp[0]
                    
                    # 현재 다리 위의 차들이 tmp[1]씩 전진했다고 생각
                    seconds -= (len(bridge) * tmp[1])
                if not (len(bridge) + 1 <= bridge_length):
                    seconds += 1
                
                    # 현재 다리 위의 차들이 모두 1씩 전진했다고 생각
                    seconds -= len(bridge)
                    
                    if bridge[0][1] <= 0:
                        tmp = bridge.popleft()
                        now_bridge_weight -= tmp[0]
                        
    if bridge:
        return seconds + bridge[-1][1]
    return seconds
    
print(solution(2, 10, [7,4,5,6]))


# 7이 들어옴 s + 1, s - 0
# 7이 빠짐   s + 1, s - 0

# 4가 들어옴 s + 1, s - 0
# 5가 들어옴 s + 1, s - 1(4가 한칸갔으니까 4 빠질 때 계산)

# 4가 빠짐   s + 2, s - 2 # 여기 2가 아니라 1이 되도록 해야함 (5가 한칸 갔으니까 5 빠질 때 계산)
# 5가 빠짐   s + 2, s - 0
 
