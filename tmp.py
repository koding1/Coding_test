from datetime import datetime, timedelta

# start ~ start + 1 사이에 tmp가 해당하는지 검사
def check(s, tmp):
    
    e = s + timedelta(seconds=1)
    # print("-------------------")
    # print(s)
    # print(e)
    # print(tmp[0])
    # print(tmp[1])
    # print("-------------------")
    # 왼쪽 선에 걸친 경우
    if s >= tmp[0] and s <= tmp[1]:
        print("T1")
        return True
    # 오른쪽 선에 걸친 경우
    if e >= tmp[0] and e <= tmp[1]:
        print("T2")
        return True
    # 박스 안에 있는 경우
    if s <= tmp[0] and e >= tmp[1]:
        print("T3")
        return True
        
    print("F")
    return False
def solution(lines):
    answer = 0
    
    data = []
    
    # day 날리고 시작시간 구해서 시작시간으로 재정렬
    for i in range(len(lines)):
        
        dateFormatter = "%Y-%m-%d %H:%M:%S.%f"
        end = datetime.strptime(lines[i][:23], dateFormatter)
        tmp = float(lines[i][24:-1])
        start = end - timedelta(seconds=(tmp - 0.001))
        
        data.append([start, end, tmp])

    
    for i in range(len(data)):
        max_tmp = 0
        
        for j in range(len(data)):
            # 시작시간과 검사할 데이터를 전달
            if check(data[i][0], data[j]):
                max_tmp += 1
        
        answer = max(answer, max_tmp)
    return answer
    
print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))

# https://programmers.co.kr/learn/courses/30/lessons/17676?language=python3
# 02.001 ~ 04.002
# 05.001 ~ 07.000
