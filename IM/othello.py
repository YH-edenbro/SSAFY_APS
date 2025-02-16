T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())

    board = [[0] * N for _ in range(N)] # NxN 크기의 게임판 만들기

    center = N//2  # 보드의 가운데 인덱스 구하기

    # 보드판 중앙에 기본 세팅하기 1 : 흑돌 2 : 백돌
    board[center - 1][center] = board[center][center - 1] = 1  # 흑돌 세팅
    board[center - 1][center - 1] = board[center][center] = 2  # 백돌 세팅

    black_stone = white_stone = 2  # 흑돌 백돌 기본 2개

    # 8방향 델타 탐색
    dx = [[0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1]]
    # 게임 시작
    for _ in range(M):
        j, i, stone = map(int, input().split())
        # 입력받은 값 인덱스화
        i -= 1
        j -= 1

        # 입력 받은 stone에 따라 흑돌 or 백돌 1개 추가
        if stone == 1:
            black_stone += 1
        else:
            white_stone += 1
        # i,j에 돌 두기
        board[i][j] = stone

        # 내가 놓은 돌 기준으로 델타 탐색
        for di, dj in dx:
            ni, nj = i + di, j + dj
            can_flip = []  # 연속된 돌 좌표 저장

            # 연속된 돌 찾아서 좌표 저장
            while 0 <= ni < N and 0 <= nj < N and board[ni][nj] != stone and board[ni][nj] != 0:
                can_flip.append((ni, nj))
                ni += di
                nj += dj

            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == stone:
                for x, y in can_flip:
                    board[x][y] = stone
                flip_count = len(can_flip)

                if stone == 1:
                    black_stone += flip_count
                    white_stone -= flip_count
                else:
                    black_stone -= flip_count
                    white_stone += flip_count


    print(f"#{tc} {black_stone} {white_stone}")