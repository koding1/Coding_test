# 내가 작성한 코드 - deque 사용 할 필요 X, 가독성이 떨어지게 하드 코딩한 느낌이라 개인적으로 아쉽다.

from collections import deque

def solution(n, t, m, timetable):
    answer = 0
    
    # timetable을 분으로 변환한 큐
    tq = deque()
    
    # 분으로 단위 통일
    timetable = sorted(timetable)
    for i in range(len(timetable)):
        hh, mm = [int(j) for j in timetable[i].split(':')]
        mm = (hh * 60) + mm
        tq.append(mm)
    
    # 09:00 를 분으로 변환
    start = 540
    end = 540 + (n-1) * t
    for i in range(n):
        cnt = 0
        if len(tq) < m:
            return str(end // 60).rjust(2, '0') + ':' + str(end % 60).rjust(2, '0')
        while tq and cnt < m:
            # 탈 수 있다면
            if tq[0] <= start:
                cnt += 1
                # 마지막 남은 자리라면
                if (cnt == m) and (i == n - 1):
                    tmp = (tq.popleft() - 1)
                    return  str(tmp // 60).rjust(2, '0') + ':' + str(tmp % 60).rjust(2, '0')
                else:
                    print(cnt, m, i, t)
                    tq.popleft()
            else:
                break
        if (i == n - 1):
            return str(end // 60).rjust(2, '0') + ':' + str(end % 60).rjust(2, '0')
        start += t
    return answer
    
print(solution(10, 60, 45,["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))

############################################################################################
# 내가 작성한 코드 2 -> 1에 대한 개선. 아래 코드와 속도 비슷하지만 아래 코드가 조금 더 
from collections import deque

def solution(n, t, m, timetable):
    answer = 0
    
    # timetable을 분으로 변환한 큐
    tq = deque()
    
    # 분으로 단위 통일
    timetable = sorted(timetable)
    for i in range(len(timetable)):
        hh, mm = [int(j) for j in timetable[i].split(':')]
        mm = (hh * 60) + mm
        tq.append(mm)
    
    # S = 09:00 를 분으로 변환
    S = 540
    # E = 마지막 탑승 시간
    E = 540 + (n-1) * t
    for i in range(n):
        corrent = S + (i * t)
        
        if len(tq) < m:
            return '%02d:%02d' % (E//60, E%60)
                    
        if i == n - 1:
            cnt = 0
            while tq:
                if cnt < m and tq[0] <= corrent:
                    if cnt == m - 1:
                        if tq[0] <= corrent:
                            return '%02d:%02d' % ((tq[0]-1)//60, (tq[0]-1)%60)
                        else:
                            return '%02d:%02d' % (E//60, E%60)
                    cnt += 1
                    tq.popleft()
                else:
                    return '%02d:%02d' % (E//60, E%60)

        else:
            cnt = 0
            while tq:
                if cnt < m and tq[0] <= corrent:
                    cnt += 1
                    tq.popleft()
                else:
                    break
##############################################################################################################
# 효율적인 코드 (속도가 더 빠름)
def solution(n,t,m,timetable):
    # 시간을 분으로
    timetable=[int(i[:2])*60+int(i[3:]) for i in timetable]
    # 정렬
    timetable.sort()
    
    # 버스 도착 시간 테이블
    bustable=[9*60+t*i for i in range(n)]
    
    for i in bustable:
        # timetable에서 기준 도착 시간 i 보다 작은 것들 모두 passenger 에 대입
        passenger=[p for p in timetable if p <= i]
        
        # 가장 오른쪽 원소와 i가 같다면 == (i == bustable[-1](마지막 시간 대))
        if i==bustable[-1]:
            # 자리가 모자란 경우 (모든 passenger가 탈 수 없음)
            if len(passenger)>=m:
                answer=passenger[m-1]-1
            # 자리가 남는 경우
            elif len(passenger)<m:
                answer=i
            # 이 케이스가 있을 수 있나 ?
            else:
                answer=passenger[-1]
        # 마지막 시간 대가 아니고, passenger를 다 태울 수 있다면
        elif len(passenger)<m:
            # passenger list를 timetable에서 모두 삭제 처리
            timetable=timetable[len(passenger):]
        # 마지막 시간 대가 아니고, passenger를 모두 태울 수 없다면
        elif len(passenger)>=m:
            # 태울 수 있는 passenger list 를 timetable에서 삭제 처리
            timetable=timetable[m:]
    answer= str(divmod(answer,60)[0]).rjust(2,'0')+':'+str(divmod(answer,60)[1]).rjust(2,'0')
    return answer
