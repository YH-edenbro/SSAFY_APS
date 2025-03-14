# 정식이 문제

def chage_num(bin_lst, ter_lst, b_i, t_i):
    global ans
    if bin_to_dec(bin_lst) == ter_to_dec(ter_lst):
        ans = bin_to_dec(bin_lst)
        return

    if b_i == len(bin_lst) or t_i == len(ter_lst):
        return

    bin_lst[b_i] = 1 - bin_lst[b_i]
    chage_num(bin_lst, ter_lst, b_i + 1, t_i)

    ter_lst[t_i] = 2 - ter_lst[t_i]
    chage_num(bin_lst, ter_lst, b_i, t_i + 1)

    if ter_lst[t_i] == 2:
        ter_lst[t_i] = 1
    else:
        ter_lst[t_i] += 1
    chage_num(bin_lst, ter_lst, b_i, t_i + 1)


def bin_to_dec(bin_n):
    bin_dec = 0
    for i in range(len(bin_n)):
        bin_dec += bin_n[i] * (2 ** (len(bin_n) - 1 - i))
    return bin_dec


def ter_to_dec(ter_n):
    ter_dec = 0
    for j in range(len(ter_n)):
        ter_dec += ter_n[j] * (2 ** (len(ter_n) - 1 - j))
    return ter_dec


T = int(input())
for tc in range(1, T+1):
    bin_num = list(map(int, list(input())))
    ter_num = list(input())
    ans = 0
    chage_num(bin_num, ter_num, 0, 0)

    print(f"{tc} {ans}")