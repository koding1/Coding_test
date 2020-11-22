from collections import deque

# 가로 세로 높이
M, N, H = map(int, input().split(' '))

box = [[list(map(int, input().split(' '))) for i in range(N)] for j in range(H)]


def BFS(box):
  ripe = 0
  underripe = 0
  empty = 0

  day = 0

  dx = [1, -1, 0, 0, 0, 0]
  dy = [0, 0, 1, -1, 0, 0]
  dh = [0, 0, 0, 0, 1, -1]

  queue = deque()

  for i in range(H):
    for j in range(N):
      for k in range(M):
        if box[i][j][k] == 1:
          queue.append([i, j, k])
          ripe += 1
        elif box[i][j][k] == 0:
          underripe += 1
        else:
          empty += 1
  
  while queue:
    tmp = True
    num = len(queue)

    for _ in range(num):
      item = queue.popleft()
    
      for i in range(6):
        mx = item[2] + dx[i]
        my = item[1] + dy[i]
        mh = item[0] + dh[i]

        if (mx >= 0 and mx < M) and (my >= 0 and my < N) and (mh >= 0 and mh < H):
          if box[mh][my][mx] == 0:
            # 해당 날이 시작하고 새로 익힌 과일이 있을 때 day 증가.
            # 처음부터 1로 다 채워진 박스를 상상했을 때 이 경우 증가하지 않도록 해야함
            if tmp:
              tmp = False
              day +=1

            queue.append([mh, my, mx])
            box[mh][my][mx] = 1
            ripe += 1
            underripe -= 1

  if ((N * M * H) - empty) == ripe:
    return day
  else:
    return -1

print(BFS(box))
