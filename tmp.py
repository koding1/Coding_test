from collections import deque

def solution(n, t, m, timetable):
    answer = 0
    timetable = sorted(timetable)
    # timetable을 분으로 변환한 큐
    tq = deque()
    
    # 분으로 단위 통일
    for i in range(len(timetable)):
        hh, mm = [int(j) for j in timetable[i].split(':')]
        mm = (hh * 60) + mm
        tq.append(mm)
    
    # 오름차순 정렬
    # tq = sorted(tq)
    # print(tq)
    
    # 09:00 를 분으로 변환
    start = 540
    for i in range(n):
        cnt = 0
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
            tmp = 540 + (i * t)
            return str(tmp // 60).rjust(2, '0') + ':' + str(tmp % 60).rjust(2, '0')
        start += t
    return answer
