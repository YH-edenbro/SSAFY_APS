T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    map_info = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    dx = [(0,1), (1,0), (0,-1), (-1,0)]
    def dfs(i_idx, j_idx, road, mountain, k_cnt):
        global long_road

        long_road = max(long_road, road)

        for di, dj in dx:
            ni, nj = i_idx + di, j_idx + dj

            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if map_info[ni][nj] < mountain:
                    visited[ni][nj] = 1
                    dfs(ni, nj, road+1, map_info[ni][nj], k_cnt)
                    visited[ni][nj] = 0
                elif not k_cnt and map_info[ni][nj] >= mountain:
                    for k in range(mountain-map_info[ni][nj], K+1):
                        if map_info[ni][nj] - k < mountain:
                            visited[ni][nj] = 1
                            dfs(ni, nj, road + 1, map_info[ni][nj] - k, 1)
                            visited[ni][nj] = 0



    # 2차원 배열에서 최대 값 찾기
    def find_max(arr):
        max_num = 0
        for i in range(N):
            for j in range(N):
                if arr[i][j] > max_num:
                    max_num = arr[i][j]
        return max_num

    top = find_max(map_info)

    long_road = 0
    for i in range(N):
        for j in range(N):
            if map_info[i][j] == top:
                start_i = i
                start_j = j
                visited[i][j] = 1
                dfs(start_i, start_j, 1, top, 0)
                visited[i][j] = 0

    print(f"#{tc} {long_road}")