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

# 효율적인 코드
def solution(priorities, location):
    jobs = len(priorities)
    answer = 0
    cursor = 0
    while True:
        if max(priorities) == priorities[cursor%jobs]:
            priorities[cursor%jobs] = 0
            answer += 1
            if cursor%jobs == location:
                break
        cursor += 1   
    return answer
