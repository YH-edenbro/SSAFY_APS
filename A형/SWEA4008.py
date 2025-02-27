def dfs(idx, result, plus, minus, mul, div):
    global max_value, min_value

    if idx == N:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
        return

    if plus > 0:
        dfs(idx + 1, result + numbers[idx], plus - 1, minus, mul, div)
    if minus > 0:
        dfs(idx + 1, result - numbers[idx], plus, minus - 1, mul, div)
    if mul > 0:
        dfs(idx + 1, result * numbers[idx], plus, minus, mul - 1, div)
    if div > 0:
        if result < 0:
            a = -(-result // numbers[idx])
            dfs(idx + 1, a, plus, minus, mul, div - 1)
        else:
            dfs(idx + 1, result // numbers[idx], plus, minus, mul, div - 1)


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    plus, minus, mul, div = map(int, input().split())
    numbers = list(map(int, input().split()))

    max_value = -float('inf')
    min_value = float('inf')

    dfs(1, numbers[0], plus, minus, mul, div)

    print(f"#{test_case} {max_value - min_value}")