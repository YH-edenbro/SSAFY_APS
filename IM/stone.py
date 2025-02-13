T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    stone = list(input().split())

    for _ in range(M):
        i, j = map(int, input().split())
        for k in range(1, j+1):
            if (i-1 - k) >= 0 and (i-1 + k) < N:
                if stone[i-1 -k] == stone[i-1 + k]:
                    if stone[i-1 -k] == '1':
                        stone[i-1 - k] = stone[i-1 + k] = '0'
                    else:
                        stone[i-1 - k] = stone[i-1 + k] = '1'

    print(f"#{tc} {' '.join(stone)}")