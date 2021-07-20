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

# 인상적인 코드들 (1)
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
    
# 인상적인 코드들 (2) - unpacking, itertools.product (데카르트 곱)
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
