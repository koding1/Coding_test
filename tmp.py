from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    cities = [q.lower() for q in cities]
    
    q = deque()
    
    for city in cities:
        if city in q:
            answer += 1
            if len(q) >= cacheSize:
                if q[0] != city:
                    q.remove(city)
                else:
                    q.popleft()
                
        else:
            answer += 5
            if q and len(q) >= cacheSize:
                q.popleft()
        q.append(city)
        
    return answer
