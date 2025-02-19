# 계산기2

def calculator_one(st, n):
    stack = [0] * n
    top = -1
    new_st = ''
    rank = {'*' : 2, '+' : 1}
    for i in range(n):
        if st[i] not in '+*':
            new_st += st[i]
        else:
            while top != -1 and rank[stack[top]] >= rank[st[i]]:
                new_st += stack[top]
                top -= 1
            top += 1
            stack[top] = st[i]

    while top != -1:
        new_st += stack[top]
        top -= 1

    return new_st


def calculator_two(st, n):
    stack = [0] * n
    top = -1
    for c in st:
        if c not in  '*+':
            top += 1
            stack[top] = int(c)
        else:
            if c == '*':
                op2 = stack[top]
                top -= 1
                op1 = stack[top]
                stack[top] = op1 * op2
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