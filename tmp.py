from collections import deque

def solution(m, n, board):
    answer = 0
    
    q = deque()
    q.append((0, 0))
    
    visited = [[0] * n for i in range(m)]
    visited[0][0] = 1
    
    dx = [0, 1, 0, 1]
    dy = [0, 0, 1, 1]
    
    check3 = 0
    while q:
        y, x = q.popleft()
        check = board[y][x]
        check2 = 0 
        
        if y == m-1 and x == n -1:
            if check3 == answer:
                return answer
            tmp_board = [[0] * n for i in range(m)]
            
            # for i in range(0, m):
            #     print(visited[i]) 
            # print("--------------------")
            for i in range(0, n):
                yy = m-1
                for j in range(m-1, -1, -1):
                    if 1 == visited[j][i]:
                        tmp_board[yy][i] = board[j][i]
                        yy -= 1
            
            # for i in range(0, m):
            #     print(tmp_board[i])  
            
            q.append((0, 0))
            visited = [[0] * n for i in range(m)]
            visited[0][0] = 1
            board = tmp_board.copy()
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
    
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
