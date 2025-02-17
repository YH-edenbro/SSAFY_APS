T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    fly_arr = [list(map(int, input().split())) for _ in range(N)]

    plus_spray = [[0,1], [1,0], [0,-1], [-1,0]]
    x_spray = [[1,1], [1,-1], [-1,-1], [-1,1]]
    max_fly = 0
    # + 로 스프레이 뿌릴 때
    for i in range(N):
        for j in range(N):
            s = fly_arr[i][j]
            for di,dj in plus_spray:
                for c in range(1,M):
                    ni, nj = i + di*c, j + dj*c
                    if 0 <= ni < N and 0 <= nj < N:
                        s += fly_arr[ni][nj]
                max_fly = max(max_fly, s)
    # x 로 스프레이 뿌릴 때
    for i in range(N):
        for j in range(N):
            s = fly_arr[i][j]
            for di,dj in x_spray:
                for c in range(1,M):
                    ni, nj = i + di*c, j + dj*c
                    if 0 <= ni < N and 0 <= nj < N:
                        s += fly_arr[ni][nj]
                max_fly = max(max_fly, s)

    print(f"#{tc} {max_fly}")