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
        if i < 8:
            nums[i] = tmp
        else:
            return -1
    
    return -1

print(solution(2, 11))


# 같은 로직이지만 set를 사용했을 때 훨씬 빠르다 (중복된 원소를 제거하여 필요 없는 계산 수를 줄인다) 

def solution(N, number):

    # N을 i번 만큼 사용 했을 때 만들 수 있는 숫자 리스트
    nums = [[] for i in range(8)]

    for i in range(1, 9):
        tmp = set()

        n1 = int(str(N) * i)
        tmp.add(n1)
        if n1 == number:
            return i

        for j in range(1, i):
            tmp2 = set()
            for k in nums[j]:
                for l in nums[i - j]:
                    tmp2.add(k + l)
                    tmp2.add(k - l)
                    if l != 0:
                        tmp2.add(k // l)
                    tmp2.add(k * l)
                    
            if number in tmp2:
                return i
            tmp = tmp | tmp2

        if i < 8:
            nums[i] = tmp
        else:
            return -1

    return -1
