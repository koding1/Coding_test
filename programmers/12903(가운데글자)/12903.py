# 원래 코드
def solution(s):
    N = len(s)

    # 홀 수
    if len(s) % 2 == 1:
        n = 0.5
    else:
        n = 1

    return ('').join(s[int(N/2-n):int(N/2+n)])
  

# 더 나은 코드들

# 1. -로 표현한게 인상적
def string_middle(str):
    a = len(str)
    if a % 2 == 0 :
        a = (a-2) / 2
    else :
        a = (a-1) / 2
    return str[int(a) : -int(a)]
  
# 2. wow
def string_middle(str):
    # 함수를 완성하세요

    return str[(len(str)-1)//2:len(str)//2+1]
  
  
