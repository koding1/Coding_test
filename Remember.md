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

### 14. set로 list의 중복값 모두 제거하기
    return min(len(nums)//2, len(set(nums)))
           
설명 : [1845 문제](https://programmers.co.kr/learn/courses/30/lessons/1845?language=python3)
[1845 코드](https://github.com/koding1/Coding_test/blob/main/programmers/1845(%ED%8F%B0%EC%BC%93%EB%AA%AC)-set/1845.py)

### 15. set에서 remove와 discard의 차이
    #1. 에러 발생
    s = set([5, 6, 8])
    s.remove(7)
    
    #2. 에러 발생하지 않음
    s = set([5, 6, 8])
    s.discard(7)
           
설명 : discard와 remove 모두 같은 기능을 하지만 discard() 는 지우려는 element가 없어도 정상적으로 진행한다.    

[77484 문제](https://programmers.co.kr/learn/courses/30/lessons/77484#fn1)
[77484 코드](https://github.com/koding1/Coding_test/blob/main/programmers/77484(%EB%A1%9C%EB%98%90%20%EC%88%9C%EC%9C%84)-set%2Cdiscard/77484.pyy)


### 16. divmod
    # 1번 코드
    x = n // 3
    y = n % 3
    
    # 2번 코드
    x, y = divmod(n, 3)
           
설명 : divmod(x, y) - 두 숫자를 인자로 전달 받아 첫번째 인자를 두번째 인자로 나눈 몫과 나머지를 tuple 형식으로 반환한다.    
1번과 2번 예제는 기능적으로 같지만, 작은 수에는 1번 코드가 더 빠르고, 큰 수 일수록 2번 코드가 더 빠르다.


미해결 :    
체육복  https://programmers.co.kr/learn/courses/30/lessons/42862/solution_groups?language=python3   
if i - 1 >= 0 and n[i - 1] == 2:
->
i - 1 >= 0 and n[i - 1] 처럼 인덱싱과 i-1 에 대한 체크를 한 줄에 해도 out of range 오류가 발생하지 않는건가요 ?


</br></br></br>
## 기억하고 싶은 문제  
### 1. 1697 메모이제이션 + BFS
설명 : 해당 문제는 아이디어부터, 기초적인 메모이제이션 기법을 사용했기 때문에 차후 복습하고 싶다.    
예시 : [1697](https://github.com/koding1/BOJ/tree/main/1697-(BFS)%E2%98%85)
