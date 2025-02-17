T = int(input())
for tc in range(1, T+1):
    N = int(input())

    omok = []
    # 오목 게임 진행
    for _ in range(N):
        stone = list(input())
        omok.append(stone)

    ans = 'NO'
    dx = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    for i in range(N):
        for j in range(N):
            if ans == 'YES':
                break
            if omok[i][j] == 'o':
                for di, dj in dx:
                    cnt = 1
                    if ans == 'YES':
                        break
                    for k in range(1, N):
                        if ans == 'YES':
                            break
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