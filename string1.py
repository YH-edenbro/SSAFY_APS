# 문자열 비교

def equal_str(s1, s2):
    N = len(s1)
    M = len(s2)

    for i in range(M-N-1):
        if str2[i:i+N] == str1:
            return 1
    return 0


T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    print(f"#{tc} {equal_str(str1, str2)}")