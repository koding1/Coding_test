def solution(d, budget):
    answer = 0
    
    # 오름차순 정렬
    d.sort()
    
    for i in d:
        budget -= i
        if budget >= 0:
            answer += 1
        else:
            return answer
        
    return answer
