# 계산기1 문제

def calculator_one(st, n):
    stack = [0] * 2
    top = -1
    new_st = ''
    for i in range(n):
        if st[i] != '+':
            new_st += st[i]
        else:
            top += 1
            stack[top] = st[i]
        if top == 1:
            new_st += stack[top]
            top -= 1
    if top != -1:
        new_st += stack[top]
        top -= 1

    return new_st


def calculator_two(st, n):
    stack = [0] * n
    top = -1
    for c in st:
        if c != '+':
            top += 1
            stack[top] = int(c)
        else:
            op2 = stack[top]
            top -= 1
            op1 = stack[top]
            stack[top] = op1 + op2
    return stack[top]


T = 10
for tc in range(1, T+1):
    N = int(input())
    cal = input()
    first = calculator_one(cal, N)
    result = calculator_two(first, N)
    print(f"#{tc} {result}")