def solution(lottos, win_nums):

    cnt = lottos.count(0)

    my_set = set(lottos + win_nums)
    # my_set.remove(0) 를 사용하면 my_set에 0 이 없을 때 에러가 난다.
    my_set.discard(0)

    min_num = 12 - cnt - len(my_set)
    max_num = min_num + cnt
    
    return [min(6, 7-max_num), min(6, 7-min_num)]
