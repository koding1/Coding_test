def solution(N, number):
    
    # N을 i번 만큼 사용 했을 때 만들 수 있는 숫자 리스트
    nums = [[] for i in range(8)]
    
    for i in range(1, 9):
        tmp = []
        
        n1 = int(str(N) * i)
        tmp.append(n1)
        if n1 == number:
            return i
        
        for j in range(1, i):
            tmp2 = []
            for k in nums[j]:
                for l in nums[i - j]:
                    tmp2.append(k + l)
                    tmp2.append(k - l)
                    if l != 0:
                        tmp2.append(k // l)
                    tmp2.append(k * l)
                    
                    if number in tmp2:
                        return i
            tmp = tmp + tmp2
        nums[i] = tmp
    
    return -1

print(solution(2, 11))


# 속도 차이 

def solution(N, number):
    answer = -1
    DP = []

    for i in range(1, 9):
        numbers = set()
        numbers.add( int(str(N) * i) )
        
        for j in range(0, i-1):
            for x in DP[j]:
                for y in DP[-j-1]:
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(x * y)
                    
                    if y != 0:
                        numbers.add(x // y)

        if number in numbers:
            answer = i
            break
        
        DP.append(numbers)

    return answer
