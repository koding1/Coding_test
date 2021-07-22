from collections import deque

def solution(tickets):
    answer = []
    
    # n + 1 == 전체 도시의 수
    n = len(tickets)
    
    q = deque()
    
    q.append(['starting','ICN', tickets, ['ICN']])
    
    while q:
        # end 는 현재 내 위치라고 생각해도 무방 (이미 도착했다고 생각)
        start, end, ticket, visited = q.popleft()
        
        # 사용 할 수 있는 티켓이 없다면
        if not ticket:
            return visited
        
        can_list = []
        for i in range(0, len(ticket)):
            # 현재 내 위치(end)에서 탈 수 있는 비행기 조회
            if (ticket[i][0] == end):
                can_list.append(ticket[i][1])
                
        # can_list 에 원소가 있다면
        if can_list:
            can_list.sort()
            tmp = can_list[0]
            del_index = ticket.index([end, tmp])
            q.append([end, tmp, (ticket[:del_index]+ticket[del_index+1:]), (visited + [tmp])])
                
    return visited
    
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# https://programmers.co.kr/learn/courses/30/lessons/43164
