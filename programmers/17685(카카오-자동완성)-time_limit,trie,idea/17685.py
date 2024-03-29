# 내 코드 

def solution(words):
    # 사전 순 정렬 후에는 좌, 우 중에 가장 가까운 문자열이 배치된다.
    # 좌, 우 두 번만 검사하면 되므로 time limit 안에 통과 가능
    words = sorted(words)
    #print(words)
    answer = 0
    
    for index, word1 in enumerate(words):
        max_ = -1
        
        tmp = []
        if index - 1 >= 0:
            tmp.append(words[index-1])
        if index + 1 < len(words):
            tmp.append(words[index+1])
        for word2 in tmp:
            i = 0
            while (word1 != word2) and (i < len(word1) and i < len(word2)) and (word1[i] == word2[i]):
                i += 1
            
            if i >= len(word1):
                max_ = i
            elif max_ < i + 1:
                max_ = i + 1
        
        #print(max_)
        answer += max_
            
    return answer

print(solution(["word", "war", "warrior", "world"]))

# Trie 자료 구조 사용
# 아직 이해 못함
