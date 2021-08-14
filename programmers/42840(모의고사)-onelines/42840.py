def solution(answers):
    top_scorer = []

    p1_answer_list = [1,2,3,4,5]
    p2_answer_list = [2,1,2,3,2,4,2,5]
    p3_answer_list = [3,3,1,1,2,2,4,4,5,5]
    
    #person 1, 2, 3 각각 의 정답 수
    answer_cnt = {1 : 0, 2 : 0, 3 : 0}
    
    for index, answer in enumerate(answers):
        p1_answer = p1_answer_list[index%5]
        p2_answer = p2_answer_list[index%8]
        p3_answer = p3_answer_list[index%10]
        
        #print(p1_answer, p2_answer, p3_answer)
        if answer == p1_answer : answer_cnt[1] += 1 
        if answer == p2_answer : answer_cnt[2] += 1 
        if answer == p3_answer : answer_cnt[3] += 1 
    
    # 기준점
    threshhold = max(answer_cnt.values())
    [top_scorer.append(index) for index, value in answer_cnt.items() if value == threshhold]
    
    return top_scorer
    
print(solution([1,2,3,4,5]))
