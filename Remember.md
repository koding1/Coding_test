# 목차

## 기억하고 싶은 알고리즘    
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

### 4. BFS
예시 : [2178](https://www.acmicpc.net/problem/2178)    

### 5. 공백없는 문자열 한글자씩 리스트에 나누어 입력 받기
        1. my_list = [list(map(int, input()))]    
        
        2. maze = [list(map(int, input())) for _ in range(N)]
        
예시 : [2667](https://www.acmicpc.net/problem/2667)
[2178](https://www.acmicpc.net/problem/2178) 

### 6. 한 줄에 여러 개의 변수 입력 받기
        1. M, N, K = [int(x) for x in input().split(' ')]
        
        2. M, N, K = map(int, input().split(' '))    
        
설명 : 공백 문자를 기준으로 각각 M, N, K 변수에 대입     
( 3 8 92 식으로 입력된다고 가정하면 M == 3, N == 8, K == 92 가 된다. )    
예시 : [1012](https://www.acmicpc.net/problem/1012)

### 7. 큐 생성
        from collections import deque
        queue = deque()
설명 : collections 라이브러리에 deque 함수를 사용한다.    
참조 : [블로그 1](https://ooeunz.tistory.com/31)

### 8. empty list check ( 빈 리스트 확인 )
        if my_list:
            print("해당 리스트는 비어있지 않습니다.")
        else: # (if not my_list)
            print("해당 리스트는 비어있습니다.")
설명 : 빈 sequence(스트링이나 리스트, 튜플)는 false값을 가진다.    

### 9. if condition one-liner
    if x > 0:
        print("x > 0 입니다.")
    else:
        print("x <= 0 입니다.")

    print("x > 0 입니다.") if x > 0 else print("x <= 0 입니다.")
설명 : 위의 if-else 문과 아래 if-else 문은 동일한 기능을 한다.  

### 10. isalpha, isdigit, isalnum
    my_string.isalpha()
    
    my_string.isdigit()
    
    my_string.isalnum()
설명 : 해당 스트링이 각각 알파벳인지, 숫자인지, 알파벳 or 숫자 인지 판단하여 True, False 를 return 한다.

### 11. zip - 여러 리스트를 for 문에 함께 사용하기
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]

    for x, y in zip(list1, list2):
        print(x, y)

### 12. 정규표현식
    from re import sub

    def solution(new_id):
        new_id = new_id.lower()
        new_id = sub("[^a-z0-9-_.]", "", new_id)
        new_id = sub("\.+", ".", new_id)
        new_id = sub("(^\.|\.$)", "", new_id)
        new_id = new_id if new_id else "a"
        new_id = sub("\.$", "", new_id[:15])
        new_id = new_id if len(new_id) > 3 else new_id + new_id[-1] * (3 - len(new_id))
        return new_id
        
설명 : https://programmers.co.kr/learn/courses/30/lessons/72410

### 13. dictionary의 key, item을 list로 return
    list(d.keys())[0]
        
예제 : https://programmers.co.kr/learn/courses/30/lessons/42576

</br></br></br>
## 기억하고 싶은 문제  
### 1. 1697 메모이제이션 + BFS
설명 : 해당 문제는 아이디어부터, 기초적인 메모이제이션 기법을 사용했기 때문에 차후 복습하고 싶다.    
예시 : [1697](https://github.com/koding1/BOJ/tree/main/1697-(BFS)%E2%98%85)
