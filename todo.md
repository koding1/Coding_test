https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    answer = 0
    
    position = 0
    name = list(name)
    current = ["A" for i in range(len(name))]

    i = 0
    cnt = 0
    while current != name:
        if current[i] != name[i]:
            # 'A'와 더 가깝다면
            if abs(ord('A') - ord(name[i])) <= abs(ord('Z') - ord(name[i])):
                cnt += abs(ord('A') - ord(name[i]))
            else:
                cnt += abs(ord('Z') - ord(name[i])) + 1
            current[i] = name[i]
        # 다음 i를 왼쪽으로 갈지 오른쪽으로 갈지 결정해야한다.
        
    return answer
    
    
print(solution("JAN"))
