# 오셀로 미완성

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 빈 보드 만들기
    board = [[0] * N for _ in range(N)]

    # 기본 세팅하기 (흑돌의 색 : 1, 백돌의 색 : 2)
    center = N//2  # 보드의 중앙 인덱스
    board[center][center - 1] = board[center - 1][center] = 1  # 흑돌
    board[center - 1][center - 1] = board[center][center] = 2  # 백돌

    # 검은색 돌과 흰색 돌 기본으로 2개씩
    black_stone = 2
    white_stone = 2
    # 게임 입력 받기
    for _ in range(M):
        i, j, stone = map(int, input().split())
        # 주어진 i, j 기준으로 검사하기
        # i, j가 인덱스가 아니어서 인덱스형태로 만들기
        i -= 1
        j -= 1
        # 검은돌을 뒀을 때
        if stone == 1:
            board[i][j] = 1
            black_stone += 1
            for row, col in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
                for k in range(1, N-1):
                    ni, nj = i+row*k, j+col*k
                    if 0 < ni < N and 0 < nj < N:
                        if board[ni][nj] == 1:
                            black_stone += 1
                            white_stone -= 1

        # 흰돌을 뒀을 때
        else:
            board[i][j] = 2
            white_stone += 1
            for row, col in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
                for k in range(1, N-1):
                    ni, nj = i+row*k, j+col*k
                    if 0 < ni < N and 0 < nj < N:
                        if board[ni][nj] == 2:
                            white_stone += 1
                            black_stone -= 1


    print(f"#{tc} {black_stone} {white_stone}")
    print(board)


# 오목 미완성

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    omok = []
    # 오목 게임 진행
    for _ in range(N):
        stone = list(input())
        omok.append(stone)

    ans = 'NO'

    for i in range(N):
        for j in range(N):
            if omok[i][j] == 'o':
                for di, dj in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
                    cnt = 1
                    if ans == 'YES':
                        break
                    for k in range(N-1):
                        ni, nj = i + di*k, j + dj*k
                        if 0 <= ni < N and 0 <= nj < N:
                            if omok[ni][nj] == '.':
                                break  # for k
                            elif omok[ni][nj] == 'o':
                                cnt += 1
                                if cnt == 5:
                                    ans = 'YES'
                                    break  # for k


    print(f"#{tc} {ans}")

