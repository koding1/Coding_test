import sys
read = sys.stdin.readline()
display_map = list(map(int, read.split(' ')))
r = display_map[2] - display_map[0]
c = display_map[3] - display_map[1]

arr = [[0] * (c + 1) for _ in range(r + 1)]

def print_arr(arr, max_length):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            preaty_str = ' ' * (max_length - len(str(arr[i][j])))
            print(preaty_str + str(arr[i][j]), end = ' ')
        print()

def is_promising(x, y, display_map):
    if (display_map[0] <= y <= display_map[2]) and (display_map[1] <= x <= display_map[3]):
        return True
    return False

def move_and_level_modify(x, y, direction, level, num, prev):

    hx = [1, 0, -1, 0]
    hy = [0, -1, 0, 1]
    
    if (direction == 0) and (num == (prev + (8 * level))): # 오른쪽으로 이동하고, 현재 넣을 숫자가 (2 + (8 * level)) 이라면 -> 오른쪽으로 뚫을 때 2 10 26 으로 뚫림
        x += hx[direction]
        y += hy[direction]
        direction = 1 # 오른 쪽으로 뚫은 이후에는 항상 위로 이동함
        return x, y, level + 1, direction, num
    
    tx = abs(x + hx[direction])
    ty = abs(y + hy[direction]) 
    if ((tx == level) and (ty <= level)) or ((tx <= level) and (ty == level)): # level 범위에 있는 경우
        x += hx[direction]
        y += hy[direction]
    else:
        direction = (direction + 1) % 4
        x += hx[direction]
        y += hy[direction]

    return x, y, level, direction, prev
    


def fill_arr(arr, r, c, display_map):
    arr_size = max(r + 1, c + 1) # 정사각형 길이 찾기
    x, y = 0, 0

    max_length = 0 # 최대 숫자 길이(자리수)
    num = 1 # 삽입할 숫자
    insert_cnt = 0 # 삽입한 횟수
    level = 0 # 몇 번째 정사각형을 만들고 있는지
    direction = 0 # 0 ~ 4 : 우 상 좌 하
    prev = 2
    while insert_cnt < ((r + 1) * (c + 1)):
        if is_promising(x, y, display_map):
            insert_cnt += 1
            arr[y - display_map[0]][x - display_map[1]] = num
            max_length = len(str(num)) if len(str(num)) > max_length else max_length
        num += 1
        x, y, level, direction, prev = move_and_level_modify(x, y, direction, level, num, prev)
    return max_length


max_length = fill_arr(arr, r, c, display_map)
print_arr(arr, max_length)
