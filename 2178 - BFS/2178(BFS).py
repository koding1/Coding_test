from collections import deque

N, M = [int(x) for x in input().split(' ')]

maze = [list(map(int, input())) for _ in range(N)]

queue = deque()

def BFS(maze):

  queue.append([0, 0])

  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]

  while queue:
    item = queue.popleft()

    for i in range(4):
      mx = item[1] + dx[i]
      my = item[0] + dy[i]
      # 먼저 해당 방향에 칸이 있는지 판단
      if (mx >= 0 and mx < M) and (my >= 0 and my < N):
        # 이동이 가능하다면 해당 위치로 이동 가능한지 판단
        if maze[my][mx] == 1 and (not(my == 0 and mx == 0)):
          maze[my][mx] = maze[item[0]][item[1]] + 1
          queue.append([my, mx])


  return maze[N-1][M-1]

print(BFS(maze))
