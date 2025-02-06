# 최대 최소의 간격

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    ai = list(map(int, input().split()))

    max_n = max(ai)
    min_n = min(ai)
    max_i = 0  # 최대값의 위치
    min_i = 0  # 최소값의 위치

    for i in range(n):
        if ai[i] == max_n:  # 최대값은 가장 늦게 나온 위치가 필요
            max_i = i+1
        elif ai[i] == min_n and min_i == 0:  # 최소값은 가장 먼저 나온 위치가 필요
            min_i = i+1

    # 절대값 만들어주기
    abs_i = max_i - min_i

    if abs_i < 0:
        abs_i = abs_i * -1

    print(f"#{tc} {abs_i}")

# 숫자 카드

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    ai = list(map(int, input()))

    count = [0] * (max(ai) + 1)  # ai의 최대값 + 1 만큼 생성

    for i in range(n):
        count[ai[i]] += 1

    lot_n = 0  # 가장 많은 숫자

    for i in range(len(count)):
        if count[i] == max(count):  # 가장 많은 숫자의 개수가 같은 경우 더 큰 숫자를 반환하기 위해 추가적인 제약 x
            lot_n = i

    print(f"#{tc} {lot_n} {max(count)}")

# 삼성시의 버스 노선

T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    # 5000개의 정류장 생성.
    cj_count = [0] * 5001

    # 각 노선 범위에 해당하는 정류장 카운트 증가
    for i in range(n):
        a, b = map(int, input().split())
        for j in range(a, b + 1):
            cj_count[j] += 1

    p = int(input())  # 조사할 버스 정류장 개수

    # 조사한 버스 정류장에 정차하는 노선의 수를 저장할 리스트
    how_many = []

    for i in range(p):
        cj = int(input())
        how_many.append(cj_count[cj])

    print(f"#{tc}", *how_many)