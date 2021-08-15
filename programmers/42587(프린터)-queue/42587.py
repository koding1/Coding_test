from collections import deque

def solution(priorities, location):
    answer = 0
    
    q = deque()
    
    for index, value in enumerate(priorities):
        tmp = 'O' if location == index else 'X'
        q.append([value, tmp])
    

    cnt = 1
    while q:
        current = q.popleft()
        check = 'X'
        for i in q:
            if current[0] < i[0]:
                check = 'O'
        
        # 자기보다 큰 수가 있을 경우 인쇄하지 않고 뒤로 보냄
        if check == 'O':
            q.append(current)
        # 자기보다 큰 수가 없고, 원하던 인쇄라면
        elif current[1] == 'O':
            return cnt 
        # 자기보다 큰 수가 없고, 원하지 않던 인쇄라면 출력
        else:
            cnt += 1
        
    return answer
    
print(solution([2, 1, 3, 2], 2))
