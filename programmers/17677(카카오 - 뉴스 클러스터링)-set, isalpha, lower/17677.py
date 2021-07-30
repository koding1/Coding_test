def solution(str1, str2):
    answer = 0
    
    # step 1. 소문자로 변환
    str1 = str1.lower()
    str2 = str2.lower()
    
    
    # step 2. 다중집합으로 변환
    s1 = []
    s2 = []
    
    for i in range(len(str1) - 1):
        tmp = str1[i] + str1[i+1]
        if tmp.isalpha():
            s1.append(tmp)
    
    for i in range(len(str2) - 1):
        tmp = str2[i] + str2[i+1]
        if tmp.isalpha():
            s2.append(tmp)
    
    # 자카드 유사도 계산
    
    # 교집합 갯수, 합집합 갯수
    a = 0
    b = 0
    # 중복 검사
    my_set = set(s1 + s2)

    for i in my_set:
        x = s1.count(i)
        y = s2.count(i)
    
        a += min(x, y)
        b += max(x, y)

    # print(a)
    # print(b)
    # print(a/b)
    if b != 0:
        return int((a/b)*65536)
    else:
        return 65536
    
print(solution('FRANCE', 'FRENCH'))
