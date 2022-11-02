def solution(survey, choices):
    answer = ''
    score = {'R': 0, 'C': 0, 'J': 0, 'A': 0, 'T': 0, 'F': 0, 'M': 0, 'N': 0}
    score2 = [3,2,1,0,1,2,3]
    
    for i in range(len(survey)):
        if choices[i] < 4:
            score[survey[i][0]] += score2[choices[i] - 1]
        elif choices[i] > 4:
            score[survey[i][1]] += score2[choices[i] - 1]
            
    if score['R'] > score['T']:
        answer += 'R'
    elif score['R'] < score['T']:
        answer += 'T'
    else:
        answer += 'R'
        
    if score['C'] > score['F']:
        answer += 'C'
    elif score['C'] < score['F']:
        answer += 'F'
    else:
        answer += 'C'
        
    if score['J'] > score['M']:
        answer += 'J'
    elif score['J'] < score['M']:
        answer += 'M'
    else:
        answer += 'J'
        
    if score['A'] > score['N']:
        answer += 'A'
    elif score['A'] < score['N']:
        answer += 'N'
    else:
        answer += 'A'
        
    return answer
