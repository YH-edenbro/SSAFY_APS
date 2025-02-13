# 괄호 검사

top = -1


def match(tx):
    global top
    stack = [0] * len(tx)  #

    for char in tx:
        if char == '({':  # 여는 괄호면 push
            top += 1
            stack[top] = char
        elif char == ')':  # 닫는 괄호면 pop
            if top == -1:
                return -1  # for char
            else:
                top -= 1
    if top > -1:
        return -1
    else:
        return 1


T = int(input())
for tc in range(1, T+1):
    txt = input()

    print(f"#{tc} {match(txt)}")

# 괄호검사( '({})' )

def match_two(tx):
    top = -1
    stack = [0] * len(tx)  #

    for char in tx:
        if char == '(' or char == '{':  # 여는 괄호면 push
            top += 1
            stack[top] = char

        elif char == ')':  # 닫는 괄호가 ')' 이면
            if top == -1 or stack[top] == '{':
                return 0
            else:
                top -= 1

        elif char == '}':  # 닫는 괄호가 '}'이면
            if top == -1 or stack[top] == '(':
                return 0
            else:
                top -= 1

        if top == len(tx):
            return 0

    if top != -1:
        return 0
    else:
        return 1


T = int(input())
for tc in range(1, T+1):
    txt = input()

    print(f"#{tc} {match_two(txt)}")

# 반복문자 지우기

def delete_seq(tx):
    N = len(tx)
    top = -1
    stack = []
    i = 0
    while i < N:

        for char in tx:
            if top == -1:  # 스택이 비어있으면
                stack.append(char)
                top += 1
                i += 1
            elif char != stack[top]:
                stack.append(char)
                top += 1
                i += 1
            else:
                stack.pop()
                top -= 1
                i += 1

    return len(stack)


T = int(input())
for tc in range(1, T+1):
    txt = input()

    print(f"#{tc} {delete_seq(txt)}")