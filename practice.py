import sys
sys.stdin = open("sample_input (1).txt", "r")


def dfs(sy_i, sy_j, a):
    global min_differ

    if sy_i == N-1 or sy_j == N-1:
        return

    if sy_i != sy_j and not visited[sy_i][sy_j] and not visited[sy_j][sy_i]:
        b = synergy[sy_i][sy_j] + synergy[sy_j][sy_i]
        visited[sy_i][sy_j] = 1
        visited[sy_j][sy_i] = 1
        min_differ = min(min_differ, abs(a-b))

    dfs(sy_i + 1, sy_j, a)

    dfs(sy_i, sy_j + 1, a)


T = int(input())

for tc in range(1, T+1):
    N = int(input())  # N: 식재료의 수
    synergy = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    min_differ = 20000  # 시너지의 최대 정수

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            A_taste = synergy[i][j] + synergy[j][i]
            dfs(0, 0, A_taste)

    print(f"{tc} {min_differ}")