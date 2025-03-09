from collections import deque

def bfs(ci, cj, h):
    global cnt
    q = deque()
    q.append((ci, cj, h))

    while q:
        ci, cj, h = q.popleft()
        if h == L:
            continue

        for di, dj in pipe_dict[(map_info[ci][cj])]:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and map_info[ni][nj] != 0 and visited[ni][nj] == 0:
                for ddi, ddj in pipe_dict[(map_info[ni][nj])]:
                    if (ddi + di, ddj + dj) == (0, 0):
                        visited[ni][nj] = 1
                        cnt += 1
                        q.append((ni, nj, h+1))



pipe_dict = {
    1: [(0,1), (1,0), (0,-1), (-1,0)],  # 상하좌우
    2: [(-1,0), (1,0)],   # 상하
    3: [(0,1), (0,-1)],   # 좌우
    4: [(-1,0), (0,1)],   # 상우
    5: [(1,0), (0,1)],    # 하우
    6: [(1,0), (0,-1)],   # 하좌
    7: [(-1,0), (0,-1)],  # 상좌
}
T = int(input())
for tc in range(1, T+1):
    # N: 터널 세로 크기, M: 터널 가로크기
    # R: 맨홀 뚜껑의 세로 좌표, C: 가로 좌표, L: 탈출 후 소요된 시간
    N, M, R, C, L = map(int, input().split())
    map_info = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    visited[R][C] = 1  # 맨홀 뚜겅 시작
    cnt = 1
    bfs(R, C, 1)

    print(f"#{tc} {cnt}")