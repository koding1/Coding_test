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
    
    # 오름차순으로 정렬, E는 기본적으로 오름차순 정렬 되어 입력된다.
    # 물론 이 과정에서 s_list[0]과 e_list[0]의 서로 짝이 달라질 수 있지만,
    # 문제가 되지 않는다.
    # s_list를 정렬하는 이유는 e_list의 특정 원소를 기준으로 해당 원소보다 작은
    # s들을 찾는 것이기 때문에 서로의 짝이 맞지 않더라도 아래 알고리즘에 문제 X
    # s_list가 있어야 e_list 의 특정 원소보다 큰 s_list 원소들을 비교하지 않을 수 있다.
    # 특정 종료 시간과 모든 시작 시간을 비교하지 않기 위해 두 개의 리스트를 만든 것
    s_list.sort()
    
    # 둘 중 하나라도 num보다 커지면 종료
    while (i < num) and (j < num):
        if s_list[i] < e_list[j]:
            cnt += 1
            max_re = max(cnt, max_re)
            i += 1
        else:
            
    
    print(s_list, e_list)
    return 0
    
print(solution([
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]))
