# 첫 작성 코드
def solution(nums):
    answer = 0

    my_list = []

    N = int(len(nums) / 2)
    for num in nums:
        if not (num in my_list):
            my_list.append(num)
            answer += 1
        if answer >= N:
          return N
    return answer


print(solution([3,1,2,3]))



# set 사용 코드

def solution(nums):
    answer = 0

    # set -> 중복된 수를 제거하여 set 자료형을 만듦
    # https://wikidocs.net/16044
    return min(len(nums)//2, len(set(nums)))
