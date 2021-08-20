# 1분 이상 1,000,000,000 분 이하라는 조건을 보고 '이진 탐색' 문제 임을 찾을 수 있음

def solution(n, times):
    # 이진 탐색의 처음 탐색 범위 : 0분 ~ 가장 길게 걸리는 시간
    start = 0
    end = max(times) * n
    
    minimum_time = end + 1

    while start <= end:
        # 이번 차례 검사할 시간(분)
        mid = (start + end)//2
        immigration_count = 0
        
        # 조건 : 모든 인원이 해당 시간에 검사를 받을 수 있는지
        # 조건에 대한 판단은 sum(mid // 심사에 걸리는 시간)과 n을 검사
        # mid // 심사 시간 은 해당 검사관이 mid분에 검사 할 수 있는 최대 인원을 의탐색의
        
        immigration_count = sum([(mid//i) for i in times])
        
        # 해당 시간(mid분) 내에 n명을 모두 검사 할 수 있다면
        if immigration_count >= n:
            end = mid - 1
            minimum_time = mid
        else:
            start = mid + 1
        
    return minimum_time
