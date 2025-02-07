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

# Flatten

for t in range(1, 11):  # 테스트 케이스 총 10개만 주어짐.

    dump = int(input())  # 덤프할 횟수 입력 받기
    box = list(map(int, input().split()))  # 박스 배열 입력 받기

    # 덤프를 진행 하는 코드
    for _ in range(dump):
        a, b = 0, 0  # 최고점 - 1, 최저점 + 1을 각각 한번만 실행할 수 있도록 a, b라는 변수로 제약.
        for j in range(100):
            if a == 0:
                if box[j] == max(box):
                    box[j] -= 1
                    a += 1
            if b == 0:
                if box[j] == min(box):
                    box[j] += 1
                    b += 1
        # 최고점 - 최저점이 1이하면 덤프를 계속하는 의미가 없기 때문에 반복문 종료.
        if (max(box) - (min(box))) <= 1:
            break

    print(f"#{t} {max(box) - min(box)}")

    # SWEA 9386 연속한 1의 개수

    T = int(input())

for tc in range(1, T+1):
    n = int(input())  # 수열의 길이
    n_list = list(map(int, input().strip()))  # 수열 입력, 앞뒤 공백 입력의 경우 예방

    
    # 연속하는 1의 개수 중 최대값을 찾는 알고리즘
    a = 0 # 연속된 1의 개수
    max_1 = 0 # 연속된 1의 개수중 최대값
    # 1이 연속되면 a는 계속 증가하는 반복문
    for i in range(n):
        if n_list[i] == 1:
            a += 1
        else:
            if max_1 < a:
                max_1 = a
                a = 0
    # 수열의 마지막이 1이고 a가 max_1보다 클 경우 최신화가 이루어지지 않으므로 조건문 한번 더 추가
    if max_1 < a:
        max_1 = a

    print(f"#{tc} {max_1}")


    # 간단한 소인수분해

    T = int(input())

for tc in range(1, T+1):
    N = int(input())

    a, b, c, d, e = 0, 0, 0, 0, 0

    while N % 11 == 0:
        N = N // 11
        e += 1

    while N % 7 == 0:
        N = N // 7
        d += 1

    while N % 5 == 0:
        N = N // 5
        c += 1

    while N % 3 == 0:
        N = N // 3
        b += 1

    while N % 2 == 0:
        N = N // 2
        a += 1

    print(f"#{tc}", a, b, c, d, e)

    # Baby-gin 게임

    T = int(input())

for tc in range(1, T+1):
    N = list(map(int, input().strip()))

    num_list = [0] * 12  # 가장 큰 수가 9, 연속된 3자리 수 검사시 인덱스에러를 피하기 위한 더미 배열 추가

    # 6개의 숫자를 순회하며 num_list에 요소의 개수 추가
    for i in range(6):
        num_list[N[i]] += 1

    tri_num = 0  # triplet의 개수
    run_num = 0  # run의 개수

    # triplet과 run이 얼마나 만들어지는지 순회하는 반복문
    i = 0
    while i < 12:
        #  triplet을 먼저 처리해야 333456 과 같은 숫자에서 놓치지 않음.
        #  333456에서 run이 먼저 처리될경우 345가 빠지고 336이 남아 baby - gin 완성을 못하게 됨.
        if num_list[i] >= 3:
            num_list[i] -= 3
            tri_num += 1
            i = 0  # 다시 i를 초기화 해줘야 같은 번호로 여러번 tri, run을 하는 것을 놓치지 않음.
        elif num_list[i] >= 1 and num_list[i+1] >= 1 and num_list[i+2] >= 1:
            num_list[i] -= 1
            num_list[i+1] -= 1
            num_list[i+2] -= 1
            run_num += 1
            i = 0
        else:
            i += 1

        if (tri_num + run_num) == 2:  # 완성됐으면 반복문 탈출
            break

    if (tri_num + run_num) == 2:
        t_f = 'true'
    else:
        t_f = 'false'

    print(f"#{tc} {t_f}")