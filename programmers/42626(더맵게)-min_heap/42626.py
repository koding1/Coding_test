import heapq

def solution(scoville, K):
    answer = 0
    
    # 최소 힙으로 변경
    heapq.heapify(scoville)
    
    # scoville에서 가장 작은 원소가 K 이상이면 종료
    while scoville[0] < K:
        if len(scoville) >= 2:
            min1 = heapq.heappop(scoville)
            min2 = heapq.heappop(scoville)
            
            heapq.heappush(scoville, min1 + (min2*2))
            answer += 1
        else:
            return -1
        
    return answer
    
    #섞은 음식의 스코빌 지수 = 
    #가장 맵지 않은 음식의 스코빌 지수 + 
    #(두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

print(solution([0, 0, 0, 0, 0, 0], 7))
