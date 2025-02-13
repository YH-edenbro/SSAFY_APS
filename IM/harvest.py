def harvest(arr, n):
    total = 0

    i = n//2
    for k in range(n//2+1):
        total += sum(arr[i][k:n-k])
        i -= 1

    i = n // 2
    for k in range(n//2+1):
        total += sum(arr[i][k:n-k])
        i += 1


    total -= sum(arr[n//2]) # 중앙이 2번 더해졌으니까 한번 빼주기

    return total

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    print(f"#{tc} {harvest(farm, N)}")