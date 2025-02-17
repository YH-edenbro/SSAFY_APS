def maximum_move(w, t, n, m):
    # 정렬 먼저 하기.
    w.sort()
    t.sort()

    total = 0
    i = n - 1
    j = m - 1
    while i >= 0 and j >= 0:
        if w[i] <= t[j]:
            total += w[i]
            i -= 1
            j -= 1
            continue
        if w[i] > t[j]:
            i -= 1
            continue
    return total


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N : 컨테이너의 수, M : 트럭의 수
    weight = list(map(int, input().split()))  # 컨테이너별로 담길 화물의 무게
    truck = list(map(int, input().split()))  # 트럭별 적재용량 정보

    print(f"#{tc} {maximum_move(weight, truck, N, M)}")