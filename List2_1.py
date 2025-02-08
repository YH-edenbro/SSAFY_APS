# 숫자를 정렬하자.

 # 카운팅 정렬렬
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    n_list = list(map(int, input().split()))

    count_list = [0] * (max(n_list) + 1)

    # 요소의 개수 세기
    for i in range(n):
        count_list[n_list[i]] += 1

    # 누적합 만들기
    for i in range(1, len(count_list)):
        count_list[i] = count_list[i] + count_list[i-1]

    # 정렬할 새로운 배열 TEMP생성 및 정렬 실행
    TEMP = [0] * n
    for i in range(n-1, -1, -1):
        count_list[n_list[i]] -= 1
        TEMP[count_list[n_list[i]]] = n_list[i]

    print(f"#{tc}", *TEMP)

# 풍선팡2 (17:14 m:s)

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [[0] * m for _ in range(n)]  # n x m 2차원 배열

    # 풍선안에 꽃가루 넣기
    for i in range(n):
        flower = list(map(int, input().split()))  # 각 행별 꽃가루 개수
        for j in range(m):
            arr[i][j] = flower[j]

    # 델타 탐색으로 꽃가루의 최대 개수 찾기
    max_f = 0
    for i in range(n):
        for j in range(m):
            balloon = arr[i][j] # 현재 풍선의 위치
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < m:
                    balloon += arr[ni][nj]  # 주변 풍선이 터졌을 때 꽃가루 더하기

            if max_f < balloon:
                max_f = balloon

    print(f"#{tc} {max_f}")

# 1209 Sum 문제

for t in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_num = 0 # 가장 큰 값
    # 각 행의 합
    for i in range(100):
        if max_num < sum(arr[i]):
            max_num = sum(arr[i])

    # 각 열의 합
    for col in zip(*arr):
        if max_num < sum(col):
            max_num = sum(col)

    # 대각선의 합
    s_l, s_r = 0, 0  # 왼쪽 대각선 s_l, 오른쪽 대각선 s_r
    for i in range(100):
        s_l += arr[i][i]
        s_r += arr[i][99-i]

    if max_num < s_l:
        max_num = s_l
    elif max_num < s_r:
        max_num = s_r

    print(f"#{t} {max_num}")

# 파리 퇴치

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]  # N x N 파리 배열 생성
    
    # 각 행에서 M만큼 슬라이싱을 하고 그 합을 행 + M 까지 더하는 코드
    most_kill = 0
    for i in range(N):
        for j in range(N):
            a = 0
            for n in range(M):
                if i+n < N and j+M <= N:
                    a += sum(arr[i+n][j:j+M])
            if most_kill < a:
                most_kill = a

    print(f"#{tc} {most_kill}")


# 색칠하기

T = int(input())

for tc in range(1, T+1):
    arr = [[0] * 10 for _ in range(10)]  # 10x10 빈 배열

    N = int(input())

    color3 = 0 # 보라색의 개수
    # 입력 받은 정보를 바탕으로 색 칠하기
    for _ in range(N):
        i1, j1, i2, j2, c = map(int, input().split())
        for i in range(i1, i2+1):
            for j in range(j1, j2+1):
                if arr[i][j] != c: # 이미 같은 색으로 칠해진 곳 중복으로 칠하지 않기
                    arr[i][j] += c
                    if arr[i][j] == 3: # 색 칠했을 때 보라색?
                        color3 += 1

    print(f"#{tc} {color3}")