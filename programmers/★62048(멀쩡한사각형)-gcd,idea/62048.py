# or import math 하여 gcd 함수 사용
def gcd(x, y):
    # y가 0이 될 때 까지
    while y:
        # y를 x에 대입
        # x를 y로 나눈 나머지를 y에 대대입
        x, y = y, x % y
    return x
  
def solution(w,h):
    
    gcd_wh = gcd(w, h)
    answer = gcd_wh * ((w//gcd_wh) + (h//gcd_wh) - 1)
    
    return (w*h) - answer
    
    
print(solution(8, 12))
