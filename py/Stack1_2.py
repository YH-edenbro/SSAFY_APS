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

# 길찾기

def dfs(s, e):
    stack = [s]
    visited = [0] * size

    while stack:
        w = stack.pop()
        if w == e:
            return 1
        if visited[w] == 0:
            visited[w] = 1
            if arr_1[w] != 0:
                stack.append(arr_1[w])
            if arr_2[w] != 0:
                stack.append(arr_2[w])
    return 0


for _ in range(1,11):
    tc, N = map(int, input().split()) # tc: test_case 번호, N: 길의 총 개수
    road = list(map(int, input().split()))

    size = 100

    # 100 사이즈의 정적배열 2개 만들기
    arr_1 = [0] * size
    arr_2 = [0] * size

    for i in range(0, len(road), 2):
        idx, route = road[i], road[i+1]
        if arr_1[idx] == 0:
            arr_1[idx] = route
        else:
            arr_2[idx] = route


    print(f"#{tc} {dfs(0, 99)}")

# 그래프 경로

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

    S, G = map(int, input().split())

    print(f"#{tc} {dfs(S, G)}")