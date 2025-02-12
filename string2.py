# 회문2

def long_palindrome(arr, N):
    # 가로 검사
    row_len = 0
    max_row_len = 1
    for row in arr:
        for j in range(N):
            for k in range(1, N-j+1):
                if row[j:j+k] == row[j+k-1:j-1:-1]:
                    row_len = k  # 회문의 길이
                max_row_len = max(max_row_len, row_len)

    # 세로 검사
    col_len = 0
    max_col_len = 1
    for col in zip(*arr):
        for j in range(N):
            for k in range(1, N-j+1):
                if col[j:j+k] == col[j+k-1:j-1:-1]:
                    col_len = k
                max_col_len = max(max_col_len, col_len)

    return max(max_col_len, max_row_len)


for _ in range(1, 11):
    tc = int(input())
    N = 100
    palindrome_arr = [input() for _ in range(N)]

    print(f"#{tc} {long_palindrome(palindrome_arr, N)}")

# 백만장자 문제

def trade_master(t, N):

    i = 0
    max_idx = 0
    profit = 0
    while i < N-1:
        # 현재 내 위치(i)보다 뒤에 가장 큰 값 찾기(더 작은 값이 나오기 전까지)
        max_price = 0
        for j in range(i, N-1):
            if max_price < t[j+1]:
                max_price = t[j+1]
                max_idx = j+1

        a = 0
        b = 0
        for k in range(i, max_idx):
            if t[k] < max_price:
                b += t[k]
                a += 1

        profit += (max_price * a) - b

        i = max_idx + 1

    return profit


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    trade = list(map(int, input().split()))

    print(f"#{tc} {trade_master(trade, N)}")