# 내 코드

def convert(n, num):
    if n == 0:
        return '0'
    # 1 ~ 15
    str_list = '0123456789ABCDEF'
    
    converted = ''
    
    while num != 0:
        converted = str_list[(num % n)] + converted
        num //= n
    
    
    return converted
    
def solution(n, t, m, p):
    answer = ''
    cnt = 0
    i = 0
    order = 1
    # 튜브의 순서인지 체크 -> (i - p) % m == 0
    
    # t개의 숫자를 구할 때 까지
    while cnt < t:
            
        num = i
        # 숫자가 바뀔 때 마다 매번 convert를 해줘야 하는가?
        tmp = convert(n, i)
        
        for s in tmp:
            print(s)
            if (order - p) % m == 0:
                if cnt >= t:
                    break
                cnt += 1
                answer += s
            order += 1
        i += 1
        converted = ''

        
    return answer
    
print(solution(16, 16, 2, 1))

###############################################################################################

# 다른 코드

DIGITS = list('0123456789ABCDEF')

def n2base(n, base):
    if n == 0:
        return DIGITS[0]

    # 각 자리수에 해당하는 문자열을 담을 리스트
    digits = []
    while n > 0:
        # 제일 마지막 자리의 숫자 구하기. 예를 들어 1658이면 '8'
        digits.append(DIGITS[n % base])
        # 제일 마지막 자리 제거. 예를 들어 1658이면 165로
        n = int(n // base)

    # 뒤집어서 반환. 예를 들어 '8561'이면 '1658'
    return ''.join(digits[::-1])


def solution(n, t, m, p):
    digits = []
    turn = 0
    while len(digits) < t * m:
        digits += list(n2base(turn, n))
        turn += 1
    # 이거 슬라이싱이 진짜 기가 막히네요...
    return ''.join(digits[p-1::m][:t])
