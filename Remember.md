# 기억하고 싶은 내용들

### 1. 재귀 제한 해제

    import sys    
    sys.setrecursionlimit(2600)

&nbsp;예시 : [1012](https://www.acmicpc.net/problem/1012)

### 2. 2차원 배열 초기화
  
    ground =  [[0] * M for _ in range(N)]

&nbsp;예시 : [1012](https://www.acmicpc.net/problem/1012)

### 3. DFS
예시 : [1012](https://www.acmicpc.net/problem/1012)
[2667](https://www.acmicpc.net/problem/1012)

### 4. 공백없는 문자열 한글자씩 리스트에 나누어 입력 받기
        my_list = [list(map(int, input()))]
예시 : [2667](https://www.acmicpc.net/problem/1012)

### 5. 한 줄에 여러 개의 변수 입력 받기
        1. M, N, K = [int(x) for x in input().split(' ')]
        
        2. M, N, K = map(int, input().split(' '))    
        
설명 : 공백 문자를 기준으로 각각 M, N, K 변수에 대입     
( 3 8 92 식으로 입력된다고 가정하면 M == 3, N == 8, K == 92 가 된다. )    
예시 : [1012](https://www.acmicpc.net/problem/1012)

### 6. 큐 생성
        from collections import deque
        queue = deque()
설명 : collections 라이브러리에 deque 함수를 사용한다.    
참조 : [블로그 1](https://ooeunz.tistory.com/31)
