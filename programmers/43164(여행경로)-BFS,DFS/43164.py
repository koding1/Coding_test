# BFS - queue
from collections import deque

def solution(tickets):
    answer = []
    
    # n + 1 == 전체 도시의 수
    n = len(tickets)
    
    q = deque()
    
    q.append(['starting','ICN', tickets, ['ICN']])
    
    while q:
        # now 는 현재 내 위치라고 생각해도 무방 (이미 도착했다고 생각)
        start, now, ticket, visited = q.popleft()
        
        # 사용 할 수 있는 티켓이 없다면
        if not ticket:
            return visited
        
        can_list = []
        for i in range(0, len(ticket)):
            # 현재 내 위치(now)에서 탈 수 있는 비행기 조회
            if (ticket[i][0] == now):
                can_list.append(ticket[i][1])
                
        # can_list 에 원소가 있다면
        if can_list:
            can_list.sort()
            for i in range(0, len(can_list)):
                    tmp = can_list[i]
                    del_index = ticket.index([now, tmp])
                    q.append([now, tmp, (ticket[:del_index]+ticket[del_index+1:]), (visited + [tmp])])
                
    return visited
  
# 해당 케이스를 통과하지 못했었다.
# 기존 코드(틀렸던 코드)는 can_list를 sorting 한 후 index 0 만 tmp로 지정해서 진행했다.
# 그렇게 할 경우 밑 예시에서 ICN - AAA 를 순회한 후 끝나고 만다.
print(solution([["ICN", "AAA"], ["ICN", "BBB"], ["BBB","AAA"]]))

########################################################################################

# DFS - stack(list)

def solution(tickets):
    answer = []
    
    # s is stack
    s = []
    
    s.append(["ICN", tickets, ["ICN"]])
    
    while s:
        now, ticket, visited = s.pop()
        
        # print("------------------------")
        # print(now)
        # print(ticket)
        # print(visited)
        
        if not ticket:
            return visited
        
        can = []
        for i in range(0, len(ticket)):
            if now == ticket[i][0]:
                can.append(ticket[i])

        # 비어있지 않다면        
        if can:
            # 스택임에 유의하여 알파벳 순서가 빠른 문자가 늦게 삽입 될 수 있도록 하기
            can.sort(reverse=True)
            for i in range(0, len(can)):
                tmp = can[i][1]
                remove_index = ticket.index([now, tmp])
                s.append([can[i][1], ticket[:remove_index]+ticket[remove_index+1:], visited + [tmp]])
        
    
    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

