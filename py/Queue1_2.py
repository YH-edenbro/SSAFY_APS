# 미로1

def find_goal_bfs(miro, scale):
    visited = [[0] * N for _ in range(N)]  # 방문기록 만들기
    q = deque()

    # 시작점 인덱스 찾기
    start = []
    for i in range(scale):
        for j in range(scale):
            if miro[i][j] == 2:
                start.append(i)
                start.append(j)
    q.append(start)
    dx = [[0,1], [1,0], [0,-1], [-1,0]]
    while q:
        ti, tj = q.popleft()
        if maze[ti][tj] == 3:
            return 1
        for di, dj in dx:
            ni, nj = ti + di, tj + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append([ni, nj])
                visited[ni][nj] = 1

    return 0


for _ in range(10):
    tc = int(input())
    N = 16  # 미로의 크기
    maze = [list(map(int, input())) for _ in range(N)]  # 미로 만들기

    result = find_goal_bfs(maze, N)

    print(f"#{tc} {result}")


# 미로2

from collections import deque


def find_goal_bfs(miro, scale):
    visited = [[0] * N for _ in range(N)]  # 방문기록 만들기
    q = deque()

    # 시작점 인덱스 찾기
    start = []
    for i in range(scale):
        for j in range(scale):
            if miro[i][j] == 2:
                start.append(i)
                start.append(j)
    q.append(start)
    dx = [[0,1], [1,0], [0,-1], [-1,0]]
    while q:
        ti, tj = q.popleft()
        if maze[ti][tj] == 3:
            return 1
        for di, dj in dx:
            ni, nj = ti + di, tj + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append([ni, nj])
                visited[ni][nj] = 1

    return 0


for _ in range(10):
    tc = int(input())
    N = 100  # 미로의 크기
    maze = [list(map(int, input())) for _ in range(N)]  # 미로 만들기

    result = find_goal_bfs(maze, N)

    print(f"#{tc} {result}")