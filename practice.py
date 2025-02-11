# 회문1 미완성

import sys
sys.stdin = open("input.txt", "r")


def make_palindrome(arr, N, le):

    a = 0 # 회문 개수
    # 가로 배열 회문 검사
    for i in range(N):
        for j in range(N - le):
            if arr[i][j:j+le] == arr[i][j+le-1:j-1:-1]:
                a += 1

    for j in range(N):
        for i in range(N - le):
            if arr[i:i+le][j] == arr[i+le-1:i-1:-1][j]:
                a += 1

    return a


for tc in range(1,11):
    N = 8
    long = int(input())
    palindrome = [list(map(str, input())) for _ in range(N)]

    print(f"#{tc} {make_palindrome(palindrome, N, long)}")



