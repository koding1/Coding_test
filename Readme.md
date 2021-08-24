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


### 16. 몫과 나머지를 구하는 두가지 방법 비교 - divmod(x, y)
    # 1번 코드
    x = n // 3
    y = n % 3
    
    # 2번 코드
    x, y = divmod(n, 3)
           
설명 :     
divmod(x, y) : 두 숫자를 인자로 전달 받아 첫번째 인자를 두번째 인자로 나눈 몫과 나머지를 tuple 형식으로 반환한다.    
1번과 2번 예제는 기능적으로 같지만, 작은 수에는 1번 코드가 더 빠르고, 큰 수 일수록 2번 코드가 더 빠르다.    
https://programmers.co.kr/learn/courses/4008/lessons/12732

### 17. itertools.product(데카르트 곱), '*' unpacking

예시 : https://github.com/koding1/Coding_test/blob/main/programmers/43165(%ED%83%80%EA%B2%9F%EB%84%98%EB%B2%84)-bfs,dfs/43165.py

### 18. yield 제너레이터(Generator)
![yield](./docs/yield.jpg)  
설명 : yield가 사용된 함수는 제너레이터를 반환한다.    
https://tech.ssut.me/what-does-the-yield-keyword-do-in-python/
예시 : https://github.com/koding1/Coding_test/blob/main/programmers/43163(%EB%8B%A8%EC%96%B4%EB%B3%80%ED%99%98)-bfs%2Cdfs/43163.py

### 19. rjust 
    # "00123"
    "123".rjust(5, "0")
설명 : 문자열의 길이가 첫 번째 인자가 될 때 까지 좌측부터 두 번째 인자(문자)를 삽입한다.    
https://kkamikoon.tistory.com/136
예시 : https://github.com/koding1/Coding_test/blob/main/programmers/17681(%EC%B9%B4%EC%B9%B4%EC%98%A4-%EB%B9%84%EB%B0%80%EC%A7%80%EB%8F%84)-%20%20bit_operation%2C%20rjust%2C%20replace/17681.py

### 19. upper, lower, isupper, islower
    # step 1. 소문자로 변환
    str1 = str1.lower()
설명 : 순서대로 대문자로 변환, 소문자로 변환, 모든 문자열이 대문자인지 체크, 모든 문자열이 소문자인지 체크      
예시 : https://github.com/koding1/Coding_test/blob/main/programmers/17677(%EC%B9%B4%EC%B9%B4%EC%98%A4%20-%20%EB%89%B4%EC%8A%A4%20%ED%81%B4%EB%9F%AC%EC%8A%A4%ED%84%B0%EB%A7%81)-set%2C%20isalpha%2C%20lower/17677.py

### 19. deque - maxlen
    q = deque(maxlen=0)
    print(q)
    # 오류 발생하지 않음
    q.append("city")
    print(q)
설명 : 큐를 특정 길이로 제한, 예시 문항에서 maxlen을 사용하지 않을 시, 20 line에 "q.append(city)" 부분에 캐시 크기가 0 일 때 append 하지 않도록 따로 지정해줘야 한다. 큐를 특정 길이로 제한 해놓는다면 자동으로 append 하지 않게 처리 되기 때문에 많은 경우에 유용하다.
예시 : https://github.com/koding1/Coding_test/blob/main/programmers/17680(%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%BA%90%EC%8B%9C)-cache%2C%20maxlen%2C%20LRU/17680.py

### 20. set - 교집합, 합집합 표현
    set1 = set([1,2,3,4])
    set2 = set([4,5,6,7])
    print(set1 | set2)
설명 : set 자료형에서 '|' -> 합집합, '&' -> 합집합
예시 : https://github.com/koding1/Coding_test/blob/main/programmers/17679(%EC%B9%B4%EC%B9%B4%EC%98%A4-%ED%94%84%EB%A0%8C%EC%A6%884%EB%B8%94%EB%A1%9D)-idea%2C/17679.py

### 21. sort - key를 사용해서 대소문자 구별 없이 정렬하기
    a = [ "bbb", "AAA", "DDD", "CCC", "aaa" ]
    a.sort(key=str.lower)
    print " ".join(a)
    # 출력 결과: AAA aaa bbb CCC DDD
    
    f = [["BBB", 2], ["ccc", 1], ["bbb", 1], ["BBB", 0]]
    # x[0]을 대소문자 구별없이 먼저 정렬하고, 그 후에 x[1]을 기준으로 정렬
    f.sort(key = lambda x : (x[0].lower(), x[1]))
    # -> x[0].lower() 처럼 사용 할 수도 있다. 
    # [["BBB", 0], ["bbb", 1], ["BBB", 2], ["ccc", 1]]
설명 : sort 함수에서 key = str.lower 를 사용하면 대소문자를 구별하지 않고 정렬 할 수 있다.
예시 : 

### 22. 정규 표현식 두 문장의 차이 '(' 의 유무
    files = ["img1.png", "IMg01.png", "img01.png", "IMG01.png"]
    tmp = [re.split(r"([0-9]+)", s) for s in files]
    # tmp -> [['img', '1', '.png'], ['IMg', '01', '.png'], ['img', '01', '.png'], ['IMG', '01', '.png']]
    tmp = [re.split(r"[0-9]+", s) for s in files]
    # tmp -> [['img', '.png'], ['IMg', '.png'], ['img', '.png'], ['IMG', '.png']]

설명 : sort 함수에서 key = str.lower 를 사용하면 대소문자를 구별하지 않고 정렬 할 수 있다.
예시 : 

### 23. 소수(prime number) 판단하기
![prime](./docs/prime.JPG)     
    
    import math
    # 2부터 x의 제곱근까지만 확인
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False # 소수 아님
    return True # 소수
설명 : 어떤 수 n이 소수인지 확인 할 때 n의 제곱근 까지만 확인하면 된다.    
이 때 시간 복잡도는 O(N**(1/2)) 이다.
예시 : 

### 24-1. 하나의 리스트에서 모든 조합을 구하기 - from itertools import combinations
     
    # combinations(items, 3) -> items 리스트 원소 이루어진 크기가 3인 모든 조합을 구하기
    items = ['1', '2', '3', '4',]
    print(combinations(itmes, 3))
    # [('1', '2', '3'), ('1', '2', '4'), ('2', '3', '4')]
    
설명 : combinations(nums, 3) -> nums 리스트 원소 이루어진 크기가 3인 모든 조합을 구하기    
예시 : https://github.com/koding1/Coding_test/blob/main/programmers/12977(%EC%86%8C%EC%88%98%EB%A7%8C%EB%93%A4%EA%B8%B0)-combinations%2Cis_prime/12977.py

### 24-2. 두개 이상의 리스트에서 모든 조합을 구하기 - from itertools import product     
    
    from itertools import product 
    items = [['1', '2'], ['a', 'b'], ['!', '@']] 
    list(product(*items)) 
    # [('1', 'a', '!'), ('1', 'a', '@'), ('1', 'b', '!'), ('1', 'b', '@'), 
       ('2', 'a', '!'), ('2', 'a', '@'), ('2', 'b', '!'), ('2', 'b', '@')]

출처: https://ourcstory.tistory.com/414 [불로]  
설명 : combinations(nums, 3) -> nums 리스트 원소 이루어진 크기가 3인 모든 조합을 구하기    
예시 : https://github.com/koding1/Coding_test/blob/main/programmers/12977(%EC%86%8C%EC%88%98%EB%A7%8C%EB%93%A4%EA%B8%B0)-combinations%2Cis_prime/12977.py

### 25-1. gcd(최대공약수) 구하기  
    # 1.
    def gcd(x, y):
        # y가 0이 될 때 까지
        while y:
            # y를 x에 대입
            # x를 y로 나눈 나머지를 y에 대대입
            x, y = y, x % y
        return x
    # 2.
    import math
    # x, y, z 의 최대공약수
    print(math.gcd(x,y,z))

### 25-2. lcm(최소공약수) 구하기  
    # 1.
    def lcm(x, y):
        return x * y // gcd(x,y)
    # 2.
    import math
    # x, y의 최소공배수
    print(math.lcm(x,y))

### 26. heapq 라이브러리 - 최소 힙 자료구조
![heaqp](./docs/heaqp.jpg)
    
    import heaqp
    
    #힙 불변성을 유지하면서, item 값을 heap으로 푸시합니다.
    heapq.heappush(heap, item)

    # heqp에서 가장 작은 항목을 pop하고 반환 (힙 불변성 유지)
    heapq.heappop(heap)
    
    # 리스트 x를 선형 시간으로 제자리에서 힙으로 변환합니다.
    heapq.heapify(x)  
    
설명 : heapq 라이브러리를 사용한 최소 힙 자료구조 구현 ( 최대 힙은 출처 첫 번째 링크 참조 ) 
예시 : https://github.com/koding1/Coding_test/blob/main/programmers/42626(%EB%8D%94%EB%A7%B5%EA%B2%8C)-min_heap/42626.py      
출처 및 참조 :       
https://littlefoxdiary.tistory.com/3      
https://docs.python.org/ko/3/library/heapq.html         


### 27. 이분 탐색( == 이진 탐색) - Binary search
    
    while start <= end:
        # 이번 차례 검사할 시간(분)
        mid = (start + end)//2
        immigration_count = 0
        
        # 조건 : 모든 인원이 해당 시간에 검사를 받을 수 있는지
        # 조건에 대한 판단은 sum(mid // 심사에 걸리는 시간)과 n을 검사
        # mid // 심사 시간 은 해당 검사관이 mid분에 검사 할 수 있는 최대 인원을 의탐색의
        
        immigration_count = sum([(mid//i) for i in times])
        
        # 해당 시간(mid분) 내에 n명을 모두 검사 할 수 있다면 (시간을 mid 이하로 줄일 수 있음)
        if immigration_count >= n: # 왼쪽으로 범위 축소
            end = mid - 1
            minimum_time = mid
        else: # 오른쪽으로 범위 축소
            start = mid + 1
    
설명 : 이진 탐색 구현

예시 :
[43238 문제](https://programmers.co.kr/learn/courses/30/lessons/43238)      
[43238 코드](https://github.com/koding1/Coding_test/blob/main/programmers/43238(%EC%9E%85%EA%B5%AD%EC%8B%AC%EC%82%AC)-%EC%9D%B4%EB%B6%84%ED%83%90%EC%83%89%2C%ED%8C%8C%EB%9D%BC%EB%A9%94%ED%8A%B8%EB%A6%AD%EC%84%9C%EC%B9%98/43238.py)    
출처 및 참조 :       
https://sanghyeok.tistory.com/7

### 28. 병합(합병) 정렬(Merge sort) 구현
![merge](./docs/merge-sort.gif)

    def merge_sort(array):
        # 종료 조건
        if len(array) == 1:
            return array

        mid = (0 + len(array)) // 2
        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:])

        i = 0
        j = 0
        k = 0

        while True:
            if left[i] <= right[j]:
                array[k] = left[i]
                k += 1
                i += 1
            else:
                array[k] = right[j]
                k += 1
                j += 1

            if i >= len(left): # left 는 모두 삽입
                while j < len(right): # 남은 right 삽입
                    array[k] = right[j]
                    k += 1
                    j += 1
                break
            if j >= len(right): # right 는 모두 삽입
                while i < len(left): # 남은 left 삽입
                    array[k] = left[i]
                    k += 1
                    i += 1
                break

        return array
설명 : 병합 정렬(Merge sort)
예시 : https://github.com/koding1/Coding_test/blob/main/programmers/BJ/sort/2751.py     
출처 및 참조 :       
https://ko.wikipedia.org/wiki/%ED%95%A9%EB%B3%91_%EC%A0%95%EB%A0%AC       
https://assaeunji.github.io/python/2020-05-06-bj2751/
</br></br></br>


## 기억하고 싶은 문제  
### 1. 1697 메모이제이션 + BFS
설명 : 해당 문제는 아이디어부터, 기초적인 메모이제이션 기법을 사용했기 때문에 차후 복습하고 싶다.    
예시 : [1697](https://github.com/koding1/BOJ/tree/main/1697-(BFS)%E2%98%85)

### 2. 12973 짝지어 제거하기 (slice vs pop) by programmers
설명 : 해당 문제에서, 분명 처음 코드도 O(n) 만큼 반복문을 수행하는데 Stack을 사용한 코드와 시간 차이가 많이 나서 의아했었다.    
이에 궁금증이 생겨 알아보니, slice와 pop 사이의 성능 차이(속도)로 인해 발생한 문제인 것 같다.      
예시 : [12973](https://github.com/koding1/Coding_test/blob/main/programmers/12973(%EC%A7%9D%EC%A0%9C%EA%B1%B0)-stack/12973.py)

### 3. 43165 타겟 넘버 (BFS, DFS, unpacking, itertools.product(데카르트곱)) by programmers
![43165dfs](./docs/43165dfs.jpg)    

설명 : BFS, DFS 의 동작과 더불어 인상적인 코드(2) 에서 unpacking, itertools.product 를 잘 활용했다.   
BFS, DFS의 이론을 알지만 문제에서의 활용이 헷갈릴 때 참고하면 좋은 문제이다.     
예시 :
[43165 문제](https://programmers.co.kr/learn/courses/30/lessons/43165)
[43165 코드](https://github.com/koding1/Coding_test/blob/main/programmers/43165(%ED%83%80%EA%B2%9F%EB%84%98%EB%B2%84)-bfs,dfs/43165.py)

### 4. 17676 카카오 추석 트래픽 (문자열 처리, 슬라이딩 윈도우, 아이디어) by programmers
![17676](./docs/17676.jpg)    

설명 : 요청량이 변하는 순간은 각 로그의 시작과 끝 이라는 점을 떠올리는게 중요한 문제이다. 이 아이디어로 O(n^2) 의 복잡도로 해결 할 수 있고, 이는 혼자 구현 할 수 있었다.
O(nlogn)의 알고리즘이 있는데, 아직 완전히 이해하지 못했다. 따라서 추후에 마저 공부하고 싶은 문제이다.
예시 :
[17676 문제](https://programmers.co.kr/learn/courses/30/lessons/17676)
[17676 코드](https://github.com/koding1/Coding_test/blob/main/programmers/17676(%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%B6%94%EC%84%9D%ED%8A%B8%EB%9E%98%ED%94%BD)/17676.py)


### 5. 17681 카카오 비밀 지도 (비트 연산자, rjust) by programmers
![17681](./docs/17681.jpg)    

설명 : bit 연산자(이 문제에서는 '|' )를 사용하는게 핵심인 문제이다. 또한 rjust 를 처음 사용하게 된 문제여서 기억하고 싶다. 아이디어를 떠올리는 난이도는 어렵지 않았다.
예시 :
[17681 문제](https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3)
[17681 코드](https://github.com/koding1/Coding_test/blob/main/programmers/17681(%EC%B9%B4%EC%B9%B4%EC%98%A4-%EB%B9%84%EB%B0%80%EC%A7%80%EB%8F%84)-%20%20bit_operation%2C%20rjust%2C%20replace/17681.py)

### 6. 17680 카카오 캐시 (cache(LRU), maxlen) by programmers
설명 : LRU 방식의 캐시 알고리즘에 대한 참고 및 deque 객체에 maxlen을 사용한 문제이다.
예시 :
[17681 문제](https://programmers.co.kr/learn/courses/30/lessons/17680)      
[17681 코드](https://github.com/koding1/Coding_test/blob/main/programmers/17680(%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%BA%90%EC%8B%9C)-cache%2C%20maxlen%2C%20LRU/17680.py)

### 6. 17679 카카오 프렌즈4블록 (set를 이용한 합집합, idea, enumerate) by programmers
![17679](./docs/17679.jpg) 
설명 : 코드 링크에 아래 쪽 '효율적인 코드' 를 보면 된다.    
set를 이용하여 간단하게 합집합을 구현하고, enumerate를 잘 활용했다.   
인상적인 것은 블록 제거 후 재구성을 편리하게 하기 위해 행과 열을 서로 치환하여 문제를 진행한다는 아이디어이다.    
예시 :
[17679 문제](https://programmers.co.kr/learn/courses/30/lessons/17679)      
[17679 코드](https://github.com/koding1/Coding_test/blob/main/programmers/17679(%EC%B9%B4%EC%B9%B4%EC%98%A4-%ED%94%84%EB%A0%8C%EC%A6%884%EB%B8%94%EB%A1%9D)-idea%2C/17679.py)

### 7. 43238 입국심사 (이분 탐색(Binaray search), 파라메트릭 서치(Parametric search) by programmers

설명 : 이분 탐색을 깔끔하게 다룬 문제라서 기억하고 싶다.    
제한 사항(심사 시간 : 1분 ~ 1,000,000,000분)을 보고 이진 탐색이라는 키워드를 떠올려야 한다.   

파라메트릭 서치 (Parametric search) : 최적화 문제를 결정 문제(예, 아니오로 답하는 문제)로 바꾸어 해결하는 기법. '원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제'       

예시 :
[43238 문제](https://programmers.co.kr/learn/courses/30/lessons/43238)      
[43238 코드](https://github.com/koding1/Coding_test/blob/main/programmers/43238(%EC%9E%85%EA%B5%AD%EC%8B%AC%EC%82%AC)-%EC%9D%B4%EB%B6%84%ED%83%90%EC%83%89%2C%ED%8C%8C%EB%9D%BC%EB%A9%94%ED%8A%B8%EB%A6%AD%EC%84%9C%EC%B9%98/43238.py)    
참조 : https://sanghyeok.tistory.com/7
# 미해결 :    
1. match 결과에 차이가 발생하는 이유    

        st = '103D'
        # 1. <_sre.SRE_Match object; span=(0, 1), match='1'>
        print(re.match('[\d+]', st))
        # 2. <_sre.SRE_Match object; span=(0, 3), match='103'>
        print(re.match('\d+', st))
해결 : '[\d+]' 은 '숫자 여러 개 반복' 이 아니라 숫자 or '+' 이다. '\d+'나, '[\d]+' 로 쓰는 것이 옳다.

2. 정규 표현식 두 문장의 차이 '(' 의 유무     

        files = ["img1.png", "IMg01.png", "img01.png", "IMG01.png"]
        tmp = [re.split(r"([0-9]+)", s) for s in files]
        # tmp -> [['img', '1', '.png'], ['IMg', '01', '.png'], ['img', '01', '.png'], ['IMG', '01', '.png']]
        tmp = [re.split(r"[0-9]+", s) for s in files]
        # tmp -> [['img', '.png'], ['IMg', '.png'], ['img', '.png'], ['IMG', '.png']]
해결 : 그냥 그런가보다.. ㅠ 어떤 원리인지 잘 이해 안감
        
3. 멀쩡한 사각형 - gcd, idea
![620481](./docs/620481.jpg)      
빨간 네모가 총 4번 반복 된다. 이 때 '4' 는 8과 12의 gcd(최대공약수) 이다.
![620482](./docs/620482.jpg)      
또한, 한 네모 안에서 사용 할 수 없게되는 단위 사각형의 수는 가로 + 세로 - 1 이다.     
1을 빼는 이유는 겹치는 사각형 때문이다.     

아이디어가 진짜 어려웠던 문제..     
아직 대각선이 지나갈 때 가로와 세로 길이 만큼 사각형이 잘린다는 것이 잘 이해가 가지 않는다.     
코드 : https://github.com/koding1/Coding_test/blob/main/programmers/%E2%98%8562048(%EB%A9%80%EC%A9%A1%ED%95%9C%EC%82%AC%EA%B0%81%ED%98%95)-gcd%2Cidea/62048.py      
설명 : https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%A9%80%EC%A9%A1%ED%95%9C-%EC%82%AC%EA%B0%81%ED%98%95-in-python
