# 내장 함수(sum) 사용 X
def solve(a: list) -> int:
    sum_ = 0
    for i in a:
        sum_ += i
    return sum_

# sum 사용 O
def solve(a: list) -> int:
    return sum(a)
