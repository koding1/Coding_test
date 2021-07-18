# 답만 맞고 효율성 테스트 통과하지 못한 코드 (stack 사용 X)
def solution(s):

    sl = list(s)

    i = 0
    while i < len(sl)-1:
        # print(i) while 문을 몇 번 정도 도는지 확인하기 위해 출력해 보았습니다.
        if len(sl) >= 2 and sl[i] == sl[i+1]:
            sl = sl[:i] + sl[i+2:]
            if i > 0:
                i -= 1
        else:
            i += 1
        
    if sl:
        return 0
    else:
        return 1
      
# stack을 사용하여 작성
def solution(s):

    sl = []
    
    for i in s:
        if len(sl) > 0 and sl[-1] == i:
            sl.pop()
        else:
            sl.append(i)
    
    if sl:
        return 0
    else:
        return 1
