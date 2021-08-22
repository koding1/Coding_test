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
    
    
def DFS(s):
    global cnt
    if N == len(s):
        cnt += 1
        return
    
    for y in range(0, N):
        for x in range(0, N):
            if check(s, y, x):
                s.append([y, x])
                DFS(s)
                s.pop()
                
DFS([])

print(cnt)
