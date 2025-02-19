# SWEA 그래프 경로

import sys
sys.stdin = open("4871_input.txt", "r")


def dfs(s, g):
    stack = []
    visited = [0] * (V+1)

    while True:
        if s == g:
            return 1
        if visited[s] == 0:
            visited[s] = 1
        for w in graph[s]:
            if visited[w] == 0:
                stack.append(s)
                s = w
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    S, G = map(int, input().split())

    print(f"#{tc} {dfs(S, G)}")