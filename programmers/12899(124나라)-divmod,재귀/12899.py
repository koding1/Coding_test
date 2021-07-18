# 첫 작성 코드
def solution(n):
    if n == 0:
        return '0'

    my_list = []

    d = {1 : '1', 
         2 : '2', 
         0 : '4'}
    
    # 0보다 큰 어떤 수로 초기화 (do while처럼 쓰기 위함)
    x = 999999

    while x > 0:
        x = int(n / 3)
        y = (n % 3)

        my_list.insert(0, d[y])

        if y == 0:
            x -= 1
        
        n = x

        
    return ('').join(my_list)
  
 

# 더 나은 코드 ( 재귀 )

def change124(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3) 
        return change124(q) + '124'[r]
      
# 개선 점 :
# 재귀로 작성하는 것과 key 1 2 0 을 사용하는 것 보다 n-1 을 나눠서 가독성을 더 살리기
# divmod -> 몫과 나머지를 return. 작은 수에는 //와 % 가 더 빠르고 큰 수는 divmod가 더 빠르다고 함.
