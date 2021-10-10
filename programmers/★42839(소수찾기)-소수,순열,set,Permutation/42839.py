import math

def per1(arr, output, numbers, visited, depth, finish):
    
    if depth == finish:

        arr.append(int(('').join(output)))
        return
    
    else:
        for i in range(len(numbers)):
            if visited[i] == False:
                
                tmp = output.copy()
                tmp.append(numbers[i])
                
                tmp_visited = visited.copy()
                tmp_visited[i] = True
                per1(arr, tmp, numbers, tmp_visited, depth+1, finish)

def isprime(num):
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
            
    return True
            
    
def solution(numbers):
    answer = 0
    
    numbers = list(numbers)
    my_set = set()
    
    # i의 의미는 Permutation을 구성 할 원소의 수
    for i in range(1, len(numbers)+1): 
        #print(i, "개의 원소를 가진 조합 목록")
        
        visited = [False] * len(numbers)
        
        arr = []
        per1(arr, [], numbers, visited, 0, i)
        
        # set의 특성을 유지하면서 list를 set에 추가 할 수 있음
        my_set.update(arr)
        
    #print(my_set)
    for num in my_set:
        # 소수의 정의 : 1보다 크면서 1과 자신만 약수로 가지는 수
        if (num > 1) and isprime(num):
            answer += 1
            #print("소수 :", num)
                
        
    return answer
    
print(solution("17"))
