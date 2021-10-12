from collections import deque

def solution(n, edges):
    cnt = 0
    
    graph = [[] for _ in range(n+1)] 

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    visited = [False] * (n+1)
    distance = [-1] * (n+1)
    
    
    # BFS를 위한 queue 생성
    q = deque()
    
    q.append(1) # 1번 정점 삽입
    visited[1] = True
    distance[1] = 0
    
    while q:
        now = q.popleft()
        
        for i in graph[now]:
            # i 정점에 방문 한 적 없다면
            if visited[i] == False:
                q.append(i) # i 정점 삽입
                visited[i] = True
                distance[i] = distance[now] + 1
    
    
    distance.sort()
    
    for num in distance[::-1]:
        if distance[-1] == num:
            cnt += 1
        else:
            break
    
    return cnt
    
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
