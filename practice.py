# 달팽이 배열 미완성

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    snail = [x for x in range(1, N**2 + 1)]
    arr = [[0] * N for _ in range(N)]

    i, j = 0, 0
    search = 0
    arr[0][0] = 1
    a = 1
    while search < N**2:

        if 0 <= j < N and arr[i][j+1] == 0:
            while 0 <= j < N and arr[i][j+1] == 0:
                arr[i][j + 1] = snail[a]
                a += 1
                j += 1
                search += 1

        if 0 <= i < N and arr[i+1][j] == 0:
            while 0 <= i < N and arr[i+1][j] == 0:
                arr[i+1][j] = snail[a]
                a += 1
                i += 1
                search += 1

        if 0 <= j < N and arr[i][j-1] == 0:
            while 0 <= j < N and arr[i][j-1] == 0:
                arr[i][j -1] = snail[a]
                a += 1
                j -= 1
                search += 1

        if 0 <= i < N and arr[i - 1][j] == 0:
            while 0 <= i < N and arr[i - 1][j] == 0:
                arr[i - 1][j] = snail[a]
                a += 1
                i -= 1
                search += 1
            continue

        print(f"#{tc}")
        for i in range(N):
            print(*(arr[i]))



