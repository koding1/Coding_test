def solution(genres, plays):
    answer = []
    
    # 1. dict 형태로 변환
    # 1번 dict -> key : genres_name, values : [[plays 수, 고유번호], [plays 수, 고유번호]...]]
    # 2번 dict -> key : genres_name, values : 장르 별 플레이 수
    
    d1 = {}
    d2 = {}
    
    for i in range(len(genres)):
        if genres[i] in d1:
            d1[genres[i]].append([plays[i], i])
        else:
            d1[genres[i]] = [[plays[i], i]]
            
        if genres[i] in d2:
            d2[genres[i]] += plays[i]
        else:
            d2[genres[i]] = plays[i]
    
    d2 = sorted(d2.items(), key = (lambda x : x[1]), reverse=True)

    for key in d2:
        key = key[0]
        tmp = d1[key]
        tmp = sorted(tmp, key = (lambda x : x[0]), reverse=True)
        
        for i in tmp[0:2]:
            answer.append(i[1])
    
    return answer
    
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
