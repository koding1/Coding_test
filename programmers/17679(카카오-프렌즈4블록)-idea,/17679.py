# 내 코드 - Queue 사용
from collections import deque

def solution(m, n, board):
    answer = 0
    
    q = deque()
    q.append((0, 0))
    
    visited = [[0] * n for i in range(m)]
    visited[0][0] = 1
    
    # 방향 4개 (내 위치, 우측, 하단, 우측하단 대각선)
    dx = [0, 1, 0, 1]
    dy = [0, 0, 1, 1]
    
    # 전 결과와 이번 결과가 변한게 있는지 체크하는 변수 ( 변한게 없다면 더 지울 블록이 없는 상태라는 뜻)
    check3 = answer
    
    while q:
        y, x = q.popleft()
        # 방향 4개가 모두 check와 같은지 확인하기 위해 사용
        check = board[y][x]
        # 방향 4개가 모두 check와 같은지 확인하기 위해 사용 ( 모두 같다면 check2가 4가 된다)
        check2 = 0 
        
        # 우측 최하단에 도착했다면 (오른쪽 구석. 사이클 반복 후 마지막에 도착하는 곳)
        if y == m-1 and x == n -1:
            # 전 결과와 변한게 없다면 (더 이상 제거할 블록이 없음을 의미)
            if check3 == answer:
                return answer
            # 새 블록을 저장할 tmp_board
            tmp_board = [[0] * n for i in range(m)]
            
            # for i in range(0, m):
            #     print(visited[i]) 
            # print("--------------------")
            
            # 새 블록을 만드는 과정
            for i in range(0, n):
                # yy는 항상 바닥부터 시작해서, 원소를 넣고 위로 한 칸씩 올라감
                yy = m-1
                for j in range(m-1, -1, -1):
                    # 사이클 반복 후 visited는 1 or 3 이다.
                    # 1 -> 제거되지 않은 블록, 3 -> 제거된 블록
                    # 3인 경우 새 tmp_board에 넣지도 않고, yy도 넣는 위치를 바꾸지 않고 그대로인 상태
                    if 1 == visited[j][i]:
                        tmp_board[yy][i] = board[j][i]
                        yy -= 1
            
            # for i in range(0, m):
            #     print(tmp_board[i])  
            
            # 큐가 다시 동작하도록 함, (0, 0) 에서 시작
            q.append((0, 0))
            # visited 초기화
            visited = [[0] * n for i in range(m)]
            visited[0][0] = 1
            # board 재 할당
            board = tmp_board.copy()
            # 반복 후 answer와 check3를 비교하여 변한게 있는지 확인
            check3 = answer
            continue
        
        for i, j in zip(dy, dx):
            if check == 0:
                break
            if ((y+i) < m) and ((x+j) < n) and (board[y+i][x+j] == check):
                check2 += 1
            else:
                break
            
        if check2 == 4:
            tmp = 0
            for i, j in zip(dy, dx):
                # 방문 O, 제거 O
                if visited[y+i][x+j] == 3:
                    continue
                
                # 방문 X, 제거 O
                elif visited[y+i][x+j] == 2:
                    visited[y+i][x+j] = 3
                    q.append((y+i, x+j))
                    
                # 방문 O, 제거 X  
                elif visited[y+i][x+j] == 1:
                    visited[y+i][x+j] = 3
                    tmp += 1
                    
                # 방문 X, 제거 X
                else:
                    tmp += 1
                    visited[y+i][x+j] = 3
                    q.append((y+i, x+j))
            answer += tmp
        else:
            for i, j in zip(dy, dx):
                # 방문 O, 제거 O
                if (y+i < m) and (x+j < n) and visited[y+i][x+j] == 3:
                    continue
                
                # 방문 X, 제거 O
                elif (y+i < m) and (x+j < n) and visited[y+i][x+j] == 2:
                    visited[y+i][x+j] = 3
                    q.append((y+i, x+j))
                    
                # 방문 O, 제거 X  
                elif (y+i < m) and (x+j < n) and visited[y+i][x+j] == 1:
                    continue
                
                # 방문 X, 제거 X
                elif (y+i < m) and (x+j < n) and visited[y+i][x+j] == 0:
                    visited[y+i][x+j] = 1
                    q.append((y+i, x+j))

    return answer
  
  ##########################################################################################
  
# 효율적인 코드 
  
def pop_num(b, m, n):
    pop_set = set()
    # search
    for i in range(1, n):
        for j in range(1, m):
            if b[i][j] == b[i - 1][j - 1] == b[i - 1][j] == b[i][j - 1] != '_':
                # pop_set = pop_set | set([(i, j), (i - 1, j - 1), (i - 1, j), (i, j - 1)])
                # 논리합
                pop_set |= set([(i, j), (i - 1, j - 1), (i - 1, j), (i, j - 1)])
    # 제거할 원소를 0으로 표현
    for i, j in pop_set:
        b[i][j] = 0
    

    for i, row in enumerate(b):
        # 제거된 원소 수 * ['_'] 리스트를 만듦
        empty = ['_'] * row.count(0)
        
        # 제거된 원소 수 만큼의 ['-'] + 행에서 0이 아닌 원소들 순서대로 배치 된다.
        # 예시) ['C', 0, 0, 'C'] 를 변환 -> ['_', '_', 'C', 'C']
        b[i] = empty + [block for block in row if block != 0]
    # len(pop_set)은 이번 차례에 제거된 원소 수를 의미한다
    # set 자료형 이기 때문에 중복은 모두 삭제 되었음
    return len(pop_set)


def solution(m, n, board):
    count = 0

    b = list(map(list, zip(*board)))  # 행열을 서로 바꿈

    while True:
        pop = pop_num(b, m, n)
        if pop == 0: return count
        count += pop
        
        
print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
