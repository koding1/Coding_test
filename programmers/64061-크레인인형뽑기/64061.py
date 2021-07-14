# Stack
def solution(board, moves):
    answer = 0

    # 세로 크기 (정사각형 이므로 가로도 같음)
    N = len(board)

    my_list = []

    for i in moves:
        x = i-1
        y = 0
        while y < N:
            if board[y][x] != 0:
                #print("삭제 :", board[y][x])
                # 뽑은 캐릭터를 board에서 삭제
                char = board[y][x]
                board[y][x] = 0

                # 리스트에 원소가 있다면
                if my_list:
                    # 기존 리스트의 가장 top 에 있는 원소와 같은지 비교
                    if my_list[-1] == char: # 터트리기
                        answer += 2
                        my_list.pop()
                    else: # 삽입하기
                        my_list.append(char)

                # 리스트가 비어있다면 바로 삽입
                else:
                    my_list.append(char)

                break
            y += 1

    return answer
