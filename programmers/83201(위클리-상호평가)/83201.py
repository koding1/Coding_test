def solution(scores):
    answer = ''
    
    n = len(scores)
    grade = []
    # i -> 가로 (행)
    for i in range(n):
        sum_ = 0
        max_ = [scores[i][i], 0]
        min_ = [scores[i][i], 0]
        # j -> 세로 (열)
        for j in range(n):
            corrent = scores[j][i]
            sum_ += corrent
            
            # 내 자신의 평가가 아니고, min_과 동일한 점수가 있다면
            if i != j and min_[0] == corrent:
                min_[1] += 1
            elif min_[0] > corrent:
                min_ = [corrent, 0]
                
            # 내 자신의 평가가 아니고, max_과 동일한 점수가 있다면   
            if i != j and max_[0] == corrent:
                max_[1] += 1
            elif max_[0] < corrent:
                max_ = [corrent, 0]
        
        # 내 자신의 평가가 가장 최저점이며, 유일하다면
        if min_[0] == scores[i][i] and min_[1] == 0:
            sum_ -= scores[i][i]
            aver = sum_ / (n-1)
        # 내 자신의 평가가 가장 최고점이며, 유일하다면
        elif max_[0] == scores[i][i] and max_[1] == 0:
            sum_ -= scores[i][i]
            aver = sum_ / (n-1)
        else:
            aver = sum_ / n
        

        if aver  >= 90:
            grade.append('A')
        elif aver >= 80:
            grade.append('B')
        elif aver >= 70:
            grade.append('C')
        elif aver >= 50:
            grade.append('D')
        else:
            grade.append('F')

    return ('').join(grade)
