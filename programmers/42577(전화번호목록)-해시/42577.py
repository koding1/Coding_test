def solution(phone_book):
    
    # 정렬하면 for 문 1 번으로 해결 가능
    phone_book.sort()
    
    for i in range(0, len(phone_book) - 1):
            # 접두어인지 확인
          
            a = phone_book[i]
            b = phone_book[i + 1][:len(a)]
            
            if a == b:
                return False
    
    return True
    
print(solution(["12","113","12356"]))
