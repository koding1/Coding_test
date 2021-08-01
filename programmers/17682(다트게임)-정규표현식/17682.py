# ver 1 - 정규 표현식 첫 사용
import re

def solution(dartResult):
    answer = 0
    
    # 1. 3번의 시도에 대한 정보를 나눠서 저장
    dart = []
    s = 0
    tmp = []
    for i in range(len(dartResult)):
        if re.match('[0-9]', dartResult[i]):
            tmp.append(dartResult[i])
        elif re.match('[SDT]', dartResult[i]):
            tmp.append(dartResult[i])
            if i + 1< len(dartResult) and re.match('[*#]', dartResult[i+1]):
                tmp.append(dartResult[i+1])
            dart.append(tmp)
            tmp = []
        else:
            continue
    # print(dart)
    
    # 2. 점수 계산
    score_list = []
    for i in range(3):
        corrent = ('').join(dart[i])
        # if 에서 False로 처리된다
        option = ''

        score = int(('').join(re.findall('[0-9]', corrent)))
        
        bonus = re.search('[SDT]', corrent).group()
        
        option_exist_check = re.search('[#*]', corrent)
        if option_exist_check:
            option = option_exist_check.group()
        
        if bonus == 'D':
            score = (score * score)
        elif bonus == 'T':
            score = (score * score * score)
        
        if option == '*':
            score = score * 2
            # 이전에 던진 기록이 있다면
            if i != 0:
                score_list[i-1] = score_list[i-1] * 2
        elif option == '#':
            score = score * (-1)
        
        # print(score)
        score_list.append(score)
    
    return sum(score_list)
    
print(solution("1S2D*3T"))

################################################################################

