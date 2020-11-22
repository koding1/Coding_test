from collections import deque

N, K = [int(x) for x in input().split(' ')]

def BFS():
  queue = deque()
  visited = [False] * 100002
  sec = 0

  queue.append(N)

  # 큐가 빌 때 까지
  while queue:

    for _ in range(len(queue)):
      item = queue.popleft()

      if item == K:
        break

      # 메모리, 시간 초과로 추가한 로직
      if ((item * 2) <= 100000):
        if (visited[item * 2] == False):
          queue.append(item * 2)
          visited[item * 2] = True

      if ((item + 1) <= 100000): 
        if(visited[item + 1] == False):
          queue.append(item + 1)
          visited[item + 1] = True

      if (item - 1 >= 0):
        if (visited[item - 1] == False):
          queue.append(item - 1)
          visited[item - 1] = True 

    if item == K:
      break
    else:
      sec += 1

  print(sec)

BFS()
