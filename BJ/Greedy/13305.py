# 현재 위치 기름 가격보다 싼 도시까지만 충전하는 것이 베스트

# 도시 수
N = int(input())

# 도시 사이의 거리
distance = [int(i) for i in input().split(' ')]

# 도시 별 기름 가격
cost = [int(i) for i in input().split(' ')]

sum_cost = 0

current_index = 0
while current_index + 1 != N:
    # 현재 위치한 도시의 기름 가격
    now_cost = cost[current_index]
    
    # now_cost 보다 싼 도시까지의 필요 이동거리 (다음 도시까지는 이동했다고 초기화)
    need_d = distance[current_index]
    
    # 내 도시보다 싼 도시를 찾을 때 까지
    next_index = current_index + 1
    while now_cost < cost[next_index]:
        if next_index + 1 < N:
            next_index += 1
        need_d += distance[next_index-1]
    
    # 이동하기 위한 기름 충전
    sum_cost = sum_cost + (need_d * now_cost)
    
    # 이동
    current_index = next_index
    
    
print(sum_cost)
