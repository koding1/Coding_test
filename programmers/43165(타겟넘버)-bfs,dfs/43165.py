# BFS - queue 사용
from collections import deque
    
def bfs_queue(numbers, target):
    answer = 0
    under = len(numbers)
    queue = deque()

    queue.append([numbers[0], 0])
    queue.append([(-1 * numbers[0]), 0])
    
    while queue:
        v, d = queue.popleft()

        # 모든 숫자를 다 사용한 깊이 and 값 == 타겟 일 때
        if d == under-1 and v == target:
            answer += 1
        
        if d+1 < under:
            queue.append([v + numbers[d+1], d+1])
            queue.append([v + (-1 * numbers[d+1]), d+1])
    return answer


# DFS - recursion
answer = 0
def DFS(numbers, target, depth, value):
    global answer

    if depth == len(numbers) and value == target:
        answer += 1

    if depth < len(numbers):
        DFS(numbers, target, depth+1, value + numbers[depth])
        DFS(numbers, target, depth+1, value - numbers[depth])

    return
