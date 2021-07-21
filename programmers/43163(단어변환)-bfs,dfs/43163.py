# BFS
from collections import deque

# 두 단어의 같은 문자 수를 리턴
def my_fuc(word1, word2):
    tmp = 0
    for i, j in zip(word1, word2):
        if i == j:
            tmp += 1
    
    return tmp

# begin->target 으로 가는 가장 짧은 과정을 찾는 문제
def solution(begin, target, words):
    queue = deque()
    visited = [False] * len(words)
    queue.append((begin, 0))

    while queue:
        word, progress = queue.popleft()

        if word == target:
            return progress
        for i in range(0, len(words)):
            if 1 == len(word) - my_fuc(word, words[i]) and (not visited[i]):
                
                print(word, words[i], progress)
                queue.append((words[i], progress+1))
                # 방문처리
                visited[i] = True

    return 0
#############################################################################################

# DFS - recursion 
answer = 0
def is_possible_change(w1, w2):
    for i in range(len(w1)):
        # i 번째 인덱스를 빼고 봤을 때 같은 경우가 하나라도 있다면 -> 두 문자열이 하나만 다르다면
        if (w1[:i]+w1[i+1:]) == (w2[:i]+w2[i+1:]):
            return True
    return False
    
def DFS(begin, target, words, depth):
    global answer
    if begin == target:
        answer = depth
        return
        
    for i in range(0, len(words)):
        if is_possible_change(begin, words[i]):
            print(begin, words[i])
            
            # i번째 인덱스 삭제
            tmp = words.copy()
            del tmp[i]
            
            DFS(words[i], target, tmp, depth+1)
            
    return
            

# begin->target 으로 가는 가장 짧은 과정을 찾는 문제
def solution(begin, target, words):
    
    DFS(begin, target, words, 0)
    
    return answer
#############################################################################################
  
# 제너레이터 사용한 코드
from collections import deque


def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word


def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)
