# 4839 이진탐색

def binary_search_faster(total_page, page_a, page_b):
    book = [x for x in range(P+1)]

    # page_a 이진탐색으로 찾을 때 걸리는 시간
    start = 1
    end = P
    a = 0
    while start <= end:
        middle = (start + end) // 2
        if book[middle] == Pa:
            a += 1
            break
        elif book[middle] > Pa:
            end = middle
            a += 1
        else:
            start = middle
            a += 1

    # pag_b를 이진탐색으로 찾을 때 걸리는 시간
    start = 1
    end = P
    b = 0
    while start <= end:
        middle = (start + end) // 2
        if book[middle] == Pb:
            b += 1
            break
        elif book[middle] > Pb:
            end = middle
            b += 1
        else:
            start = middle
            b += 1

    if a > b:
        return 'B'
    elif a < b:
        return 'A'
    else:
        return 0


T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    print(f"#{tc} {binary_search_faster(P, Pa, Pb)}")


# 특별한 정렬

def special_sort(a, n):
    for i in range(n):
        special_index = i
        for j in range(i+1, n):
            if i % 2 == 0:
                if a[special_index] < a[j]:
                    special_index = j
            else:
                if a[special_index] > a[j]:
                    special_index = j
        a[i], a[special_index] = a[special_index], a[i]


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    special_sort(arr, n)

    print(f"#{tc}", *(arr[:10]))

# 숫자 배열 회전

# 90도 회전
def rotate_90(a):
    return list(map(list, zip(*a[::-1])))


# 180도 회전
def rotate_180(a):
    a = list(map(list, zip(*a[::-1])))
    return list(map(list, zip(*a[::-1])))


# 270도 회전(90도 반시계 회전)
def rotate_270(a):
    return list(zip(*a))[::-1]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]

    arr_90 = rotate_90(arr)
    arr_180 = rotate_180(arr)
    arr_270 = rotate_270(arr)

    print(f"#{tc}")
    for i in range(N):
        b = arr_90[i][:]
        c = arr_180[i][:]
        d = arr_270[i][:]
        print(f'{"".join(b)} {"".join(c)} {"".join(d)}')


# 풍선팡 1

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    balloon = [list(map(int, input().split())) for _ in range(N)]  # 꽃가루가 들어있는 풍선 배열

    max_flower = 0  # 최대 터지는 꽃가루
    for i in range(N):
        for j in range(M):
            flower = balloon[i][j]  # 현재 위치에 있는 풍선의 꽃가루가 몇개인지
            s = balloon[i][j]  # 현재 꽃까루까지 포함해야 하기 때문에
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:  # 상하좌우 살펴보기
                for c in range(1, flower+1):  # 풍선의 꽃가루 개수만큼 주변을 탐색
                    ni, nj = i + di * c, j + dj * c
                    if 0 <= ni < N and 0 <= nj < M:
                        s += balloon[ni][nj]
            max_flower = max(max_flower, s)

    print(f"#{tc} {max_flower}")

# Ladder1

for t in range(1, 11):
    T = int(input())
    N = 100
    ladder = [list(map(int, input().split())) for _ in range(N)]  # 사다리 배열 생성

    # 도착 지점 찾기 - 도착점부터 올라오면 시간을 줄일 수 있음
    gi, gj = N -1, 0
    for j in range(N):
        if ladder[-1][j] == 2:
            gj = j
            break

    # 위로 이동하면서 시작점 찾기
    # 마지막에 도달한 후 j 인덱스가 시작점
    while gi > 0:
        # 왼쪽으로 쭉 이동
        if gj > 0 and ladder[gi][gj - 1] == 1:
            while gj > 0 and ladder[gi][gj - 1] == 1:
                gj -= 1
            gi -= 1  # 왼쪽 쭉 이동하면 일단 한칸 위로(다시 오른쪽으로 안 가도록)
            continue

        # 오른쪽으로 쭉 이동
        if gj < N - 1 and ladder[gi][gj + 1] == 1:
            while gj < N - 1 and ladder[gi][gj + 1] == 1:
                gj += 1
            gi -= 1 # 오른쪽 쭉 이동하면 일단 한칸 위로(다시 오른쪽으로 안 가도록)
            continue

        # 왼쪽, 오른쪽에 길이 없으면 위로 이동
        gi -= 1

    print(f"#{T} {gj}")
