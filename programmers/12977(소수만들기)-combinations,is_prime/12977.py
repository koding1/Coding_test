# combinations 함수 사용 X
import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0: return False
    return True
    
def solution(nums):
    answer = 0

    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if is_prime(nums[i] + nums[j] + nums[k]): answer += 1

    return answer
    
print(solution([1,2,3,4]))

# combinations 함수 사용 O
import math
from itertools import combinations

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0: return False
    return True
    
def solution(nums):
    answer = 0
    
    # combinations(nums, 3) -> nums 리스트 원소 이루어진 
    # 크기가 3인 모든 조합을 구하기
    for num_list in combinations(nums, 3):
        if is_prime(sum(num_list)): answer += 1

    return answer
    
print(solution([1,2,3,4]))
