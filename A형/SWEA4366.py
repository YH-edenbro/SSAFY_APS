def bin_to_dec(bin_n):
    bin_dec = 0
    for i in range(len(bin_n)):
        bin_dec += bin_n[i] * (2 ** (len(bin_n) - 1 - i))
    return bin_dec

def ter_to_dec(ter_n):
    ter_dec = 0
    for j in range(len(ter_n)):
        ter_dec += ter_n[j] * (3 ** (len(ter_n) - 1 - j))  # 3진수 변환
    return ter_dec

T = int(input())
for tc in range(1, T+1):
    bin_num = list(map(int, list(input().strip())))
    ter_num = list(map(int, list(input().strip())))
    ans = 0

    for b_i in range(len(bin_num)):
        bin_num[b_i] = 1 - bin_num[b_i]

        for t_i in range(len(ter_num)):
            t = ter_num[t_i]  # 원래 3진수 값 저장
            for n in range(3):
                if t != n:
                    ter_num[t_i] = n

                    if bin_to_dec(bin_num) == ter_to_dec(ter_num):
                        ans = bin_to_dec(bin_num)
                        break
            ter_num[t_i] = t  # 원래 3진수 값 돌려주기
        bin_num[b_i] = 1 - bin_num[b_i]  # 원래 2진수 값으로 돌려주기
        if ans > 0:
            break

    print(f"#{tc} {ans}")