T = int(input())

for tc in range(1, T+1):
    N = int(input())
    balloon = [list(map(int, input().split())) for _ in range(N)]

    dx = [[0,1], [1,0], [0,-1], [-1,0]]
    max_sum = 0
    min_sum = sum(balloon[0]) + sum(list(zip(*balloon))[0])  # 초기값은 배열의 첫번째 열과 행의 합
    for i in range(N):
        for j in range(N):
            cur = balloon[i][j]
            for di, dj in dx:
                for c in range(1, N):
                    ni, nj = i + di*c, j + dj*c
                    if 0 <= ni < N and 0 <= nj < N:
                        cur += balloon[ni][nj]
            max_sum = max(max_sum, cur)
            min_sum = min(min_sum, cur)

    print(f"#{tc} {max_sum - min_sum}")