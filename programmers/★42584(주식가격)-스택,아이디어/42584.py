def solution(prices):
    N = len(prices)
    # init
    answer = [-1] * N
    
    # s is stack. (init)
    s = [0] # The meaning of 0 is 'second' and 'index'.
    
    for now in range(1, N):
        
        while s:
            # 가격이 떨어진 경우
            if (prices[now] < prices[s[-1]]):
                answer[s[-1]] = now - s[-1]
                s.pop()
            else:
                break
        s.append(now)
    
    # 스택에 남아있는 초들은 끝까지 하락이 없었던 경우들
    # 즉 끝 시간(N-1) - 해당 초 를 해주면 몇 초 동안 상승장이였는지 알 수 있음
    while s:
        top_second = s.pop()
        answer[top_second] = (N - 1) - top_second
        
    return answer
    
print(solution([1, 3, 0, 5]))
