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

# DFS - recursion
answer = 0
def DFS(n, computers, num, visited):
    global answer
    
    visited[num] = True
    
    check = visited.count(False)
    if check == 0:
        return
    # 아직 연결 확인하지 못한 컴퓨터가 여러 대(2대 이상)가 남았다면
    else:
        tmp = 0
        corrent = computers[num]
    
        for i in range(0, len(corrent)):
            if (corrent[i] == 1) and (not visited[i]):
                tmp = 1
                DFS(n, computers, i, visited)

    return

def solution(n, computers):
    global answer
    
    visited = [False] * n
    
    # 이 while 문 추가하는게 아이디어 떠올리기가 어려웠어요.
    # 보통 DFS 함수를 재귀 밖에서 호출하는 횟수가 1번이였기 때문에..
    while visited.count(False) != 0:
            answer += 1
            # 가장 앞에 있는 False의 인덱스
            i = visited.index(False)
            DFS(n, computers, i, visited)
    
    
    return answer
