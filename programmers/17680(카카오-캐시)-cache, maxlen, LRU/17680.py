# deque maxlen, cache (LRU) 
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    cities = [q.lower() for q in cities]
    
    q = deque(maxlen=cacheSize)
    
    for city in cities:
        if city in q:
            answer += 1
            q.remove(city)
        else:
            answer += 5
            if q and len(q) >= cacheSize:
                q.popleft()
               
        q.append(city)

    return answer

print(solution(0,["a", "a"]))
