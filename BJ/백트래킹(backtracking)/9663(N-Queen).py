#https://www.acmicpc.net/problem/9663

# s is stack
s = []
cnt = 0
N = int(input())

def check(s, y, x):
    for queen in s:
        # queen's y index == y
        if queen[0] == y:
            return False
        # queen's x index == x
        if queen[1] == x:
            return False
        # 대각선상에 있다면
        if abs(queen[0]-y) == abs(queen[1]-x):
            return False
    return True
    
    
def DFS(s, depth):
    global cnt
    # depth의 역할 : 1. 행(y), 2. len(s)
    if N == depth:
        cnt += 1
        return
    

    for x in range(0, N):
        if check(s, depth, x):
            s.append([depth, x])
            DFS(s, depth + 1)
            s.pop()
                
DFS([], 0)

print(cnt)
