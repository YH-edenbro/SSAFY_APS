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





