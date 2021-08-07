def solution(msg):
    answer = []
    
    # search_list
    sl = ['A', 'B', 'C', 'D' ,'E', 'F', 'G', 'H', 
    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    i = 0
    end = len(msg)
    while i < end:
        print_str = ''
        plus_str = ''
        for j in msg[i:]:
            if print_str+j in sl:
                i += 1
                print_str += j
            else:
                plus_str = print_str + j 
                break
        answer.append(sl.index(print_str) + 1)
        sl.append(plus_str)
    
    return answer
  
print(solution('KAKAO'))
