# BFS - queue
from collections import deque

def solution(n, computers):
    answer = 0
    
    n = len(computers)
    
    visited = [False] * n
    queue = deque()
    
    
    while visited.count(True) != n:
        # index 함수는 해당 원소가 없으면 error가 발생하지만, False가 있다는 것을 while 조건문에서 검증한 상태이다
        i = visited.index(False)
        # 방문하지 않는 컴퓨터가 있다면
        if not visited[i]:
            answer += 1
            queue.append(computers[i])
            visited[i] = True
                
        while queue:
            corrent = queue.popleft()
            
            for i in range(0, n):
                # 해당 컴퓨터와 연결되어 있고 방문한 적 없는 컴퓨터라면
                if (corrent[i] == 1) and (not visited[i]):
                    queue.append(computers[i])
                    visited[i] = True        
            
    return answer
  
  ##################################################################################################
