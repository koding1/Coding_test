# 기억하고 싶은 문제에 추가함

from itertools import product

def solution(clothes):
    answer = 1
    
    # key : kind, value : item count
    d = {}
    
    for item in clothes:
        # if d does not have the key item[i]
        if item[1] not in d:
            # 1로 시작하는 이유 : 해당 부위를 입지 않을 경우를 추가하기 위해서
            d[item[1]] = 1
        
        d[item[1]] += 1
    
    for num in list(d.values()):
        answer *= num
    
    return answer-1
