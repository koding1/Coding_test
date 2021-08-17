# 스택, 큐 사용하지 않은 코드
# i를 사용하는 대신 기준 되는 날로부터 q.popleft를 이용해 제거하는 식으로 짜면
# 큐와 같이 구현 가능
import math

def solution(progresses, speeds):
    answer = []
    
    i = 0
    
    while i < len(progresses):
        cnt = 0
        
        need_day = math.ceil((100 - progresses[i]) / speeds[i])
        
        while i < len(progresses) and (progresses[i]+(speeds[i]*need_day)) >= 100:
            cnt += 1
            i += 1
        
        answer.append(cnt)
        
    return answer
  

# 인상적인 코드들
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        # 큐가 비어있다 or 현재 큐에 가장 최근에 들어간 원소의 필요 일수보다 크다
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            # ex) (95-100) // 4 -> -2 여기에 -1을 곱하면 2
            # 결과적으로 math.ceil 과 동일
            Q.append([-((p-100)//s),1])
        # 큐에 원소가 있고, 큐에 가장 최근에 들어간 원소의 필요 일 수보다 작거나 같다면(같이 배포 가능)
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
  
  
