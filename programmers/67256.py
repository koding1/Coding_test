# 키패드 누르기 - 이지
def distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def solution(numbers, hand):
    answer = []

    pos = {1 : (0, 0), 2 : (1, 0), 3 : (2, 0),
           4 : (0, 1), 5 : (1, 1), 6 : (2, 1),
           7 : (0, 2), 8 : (1, 2), 9 : (2, 2),
           10: (0, 3), 0 : (1, 3), 11: (2, 3) }

    # 각 엄지 손가락의 현재 위치
    left =  pos[10]
    right = pos[11]

    for num in numbers:

        if num in [1, 4, 7]:
            answer.append('L')
            left = pos[num]

        elif num in [3, 6, 9]:
            answer.append('R')
            right = pos[num]

        #if num in [2, 5, 8, 0]:
        else:
            # 버튼과의 거리를 두 손가락에 대해 모두 계산
            ld = distance(left, pos[num])
            rd = distance(right, pos[num])

            if ld < rd:
                answer.append('L')
                left = pos[num]
            elif ld > rd:
                answer.append('R')
                right = pos[num]

            # 거리가 같다면 사용자의 주 사용 손을 검사하여 판단
            else:
                if hand == 'left':
                    answer.append('L')
                    left = pos[num]
                else:
                    answer.append('R')
                    right = pos[num]

    
    return ''.join(answer)
