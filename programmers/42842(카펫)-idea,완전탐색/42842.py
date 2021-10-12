def solution(brown, yellow):
    answer = []
    
    # 카펫 총 타일 수
    carpet = brown + yellow
    
    for i in range(1, int(carpet/2) + 1):
        # i로 나눌 수 있다면
        if carpet % i == 0:
            # i * j == carpet 이 될 수 있도록 j를 setting
            j = carpet // i
            
            # (가로*2 + 세로*2) - 4 == 브라운 타일의 갯수
            if (((i*2)+(j*2)) - 4) == brown:
                answer.append([i, j]) if i >= j else answer.append([j, i])
                break
                
        
    
    return answer[0]
