# 연습문제 3. 그래프 탐색

def dfs(v, N):
    visited = [0] * (N+1)
    stack = []
    lst = []

    while True:
        if visited[v] == 0:
            visited[v] = 1
            lst.append(v)
        for w in graph[v]:
            if visited[w] == 0:
                stack.append(v)
                v = w
                break
        else:
            if stack:
                v = stack.pop()
            else:
                return lst

tc = 1
V, E = map(int, input().split())
lst = list(map(int, input().split()))

graph = [[] for _ in range(V+1)]

for i in range(E):
    graph[lst[i*2]].append(lst[i*2 + 1])
    graph[lst[i * 2 + 1]].append(lst[i * 2])

print(f"#{tc}", '-'.join(map(str, (dfs(1,V)))))

