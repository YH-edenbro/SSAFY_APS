import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [[0] * N for _ in range(N)]  # N x N 비어있는 2차원배열 생성

    # 구역마다 파리 집어 넣기
    for i in range(N):
        fly_list = list(map(int, input().split()))
        for j in range(N):
            arr[i][j] = fly_list[j]

    most_kill = 0
    a_list = []
    b_list = []

    for i in range(N):
        for j in range(N):
            if 0 <= j+M-1 < N and 0 <= i < N:
                a = sum(arr[i][j:j+M-1])
                a_list.append(a)
        b_list.append(sum(a_list))
        a_list = []

        if most_kill < sum(b_list):
            most_kill = sum(b_list)

    print(f"{tc} {most_kill}")
