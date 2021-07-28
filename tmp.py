from datetime import datetime, timedelta

# start ~ start + 1 사이에 tmp가 해당하는지 검사
def check(s, tmp):
    
    e = s + timedelta(seconds=0.999)
    # print("-------------------")
    # print(s)
    # print(e)
    # print(tmp[0])
    # print(tmp[1])
    # print("-------------------")
    # 왼쪽 선에 걸친 경우
    if s >= tmp[0] and s <= tmp[1]:
        #print("T1")
        return True
    # 오른쪽 선에 걸친 경우
    if e >= tmp[0] and e <= tmp[1]:
        #print("T2")
        return True
    # 박스 안에 있는 경우
    if s <= tmp[0] and e >= tmp[1]:
        #print("T3")
        return True
        
    #print("F")
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
            if check(data[i][1], data[j]):
                max_tmp += 1
        
        answer = max(answer, max_tmp)
    return answer

############################################################

def solution(lines):
    
    # 시작 시간 리스트, 종료 시간 리스트
    s_list = []
    e_list = []
    for i in range(len(lines)):
        # 날짜, 시간, 트래픽 처리에 걸린 시간
        a, b, c = lines[i].split(" ")
        # 시간, 분, 초
        x, y, z = b.split(":")
        
        # 트래픽 처리에 걸린 시간 파싱
        c = float(c[:-1])
        
        second = float(x) * 3600 + float(y) * 60 + float(z)
        # 포함 구간 1초를 추가해서 삽입 (코드 간소화)
        e_list.append(second + 1)
        # 종료시간 - 걸린 시간 = 시작 시간
        s_list.append(second - c + 0.001)
        
    # i == 시작 시간 반복자, j == 종료 시간 반복자
    i, j, cnt = 0
    num = len(lines)
    
    # 오름차순으로 정렬
    s_list.sort()
    
    # 둘 중 하나라도 num보다 커지면 종료
    while (i < num) and (j < num):
        if 
        
    
    print(s_list, e_list)
    return 0
    
print(solution([
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]))
