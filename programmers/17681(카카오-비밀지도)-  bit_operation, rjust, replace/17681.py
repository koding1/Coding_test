# 비트 연산자, rjust, replace 
def solution(n, arr1, arr2):
    answer = []
    
    
    for i in range(n):
        n1 = arr1[i]
        n2 = arr2[i]
        # 비트 연산 (둘 중 하나라도 1 이라면 1)
        c = bin(n1 | n2)
        # c 예시 : 0b11011 -> 2진수를 표현하기 위해 앞에 0b가 항상 붙음
        # 따라서 index 0, 1 필요 없으니 삭제
        c = c[2:]
        
        # c 문자열의 길이가 n 이하라면 좌측부터 '0'으로 채워 길이를 n으로 만든다
        c = c.rjust(n, '0')
        
        c = c.replace('1', '#')
        c = c.replace('0', ' ')
        
        answer.append(c)
    
    return answer
    
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))
