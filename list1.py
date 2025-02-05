# SWEA min max 문제제

T = int(input())  # 테스트 케이스 개수 입력

for test_case in range(1, T+1):
    n = int(input())  # 양수의 개수 n 입력
    ai = list(map(int, input().split()))  # n개의 양수

    min_n = ai[0]
    max_n = ai[0]

    for i in range(1, n):
        if min_n > ai[i]:
            min_n = ai[i]
        elif max_n < ai[i]:
            max_n = ai[i]

    print(f'#{test_case} {max_n - min_n}')


# SWEA 구간합

T = int(input())

for test_case in range(1, T+1):

    n, m = map(int, input().split())
    ai = list(map(int, input().split()))

    m_list = []

    for i in range(n):
        if i + m > n:
            break
        m_list.append(ai[i:i+m])

    big_n = sum(m_list[0])
    small_n = sum(m_list[0])

    for item in m_list:
        if big_n < sum(item):
            big_n = sum(item)
        elif small_n > sum(item):
            small_n = sum(item)

    print(f'#{test_case} {big_n - small_n}')


# View

for test_case in range(1, 11):
    n = int(input())
    height = list(map(int, input().split()))

    window = 0

    for i in range(2, n-2):
        if height[i] > height[i-2] and height[i] > height[i+2]:
            if height[i] > height[i+1] and height[i] > height[i-1]:
                window = window + height[i] - max(height[i+1], height[i+2], height[i-1], height[i-2])

    print(f'#{test_case} {window}')






