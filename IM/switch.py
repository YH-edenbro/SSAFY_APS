def switch(a, b, n):

    cnt = 0
    i = 0
    while i < n:
        if a[i] != b[i]:
            for j in range(n-i):
                a[i+j] = 1 - a[i+j]
            cnt += 1
        i += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Ai = list(map(int, input().split()))  # 조작 전 스위치의 상태
    Bi = list(map(int, input().split()))  # 조작 후 스위치의 상태

    print(f"#{tc} {switch(Ai, Bi, N)}")