# 암호생성기

def pass_q(num_lst, n):
    q = []
    k = 1
    # 입력받은 num_lst를 q에 배치하기
    for i in range(n):
        if k == 6:
            k = 1
        q.append(num_lst[i] - k)
        if num_lst[i] - k <= 0:
            break
        k += 1

    front = 0  # 아직 뽑아낸게 없어서 0
    rear = 7  # 8개를 q에 넣어서 7
    while q[rear] > 0:
        if k == 6:
            k = 1
        q.append(q[front] - k)
        k += 1
        front += 1
        rear += 1

    if q[rear] < 0:
        q[rear] = 0

    return ' '.join(map(str, q[front:rear+1]))


for _ in range(10):
    tc = int(input())
    N = 8
    num = list(map(int, input().split()))
    result = pass_q(num, N)

    print(f"#{tc} {result}")

# 회전

def rotate(lst, m):

    cnt = 0
    while cnt != m:
        a = lst.pop(0)
        lst.append(a)
        cnt += 1
    return lst[0]



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N : 수열의 길이, M : 작업 횟수
    num_lst = list(map(int, input().split()))
    result = rotate(num_lst, M)
    print(f"#{tc} {result}")

# 피자 굽기

from collections import deque


def last_pizza(pizza, n, m):
    q = deque()
    for i in range(n):
        info = [pizza[i]//2, i+1]
        q.append(info)
    i = n
    cur = m
    while cur > 1:
        a = q.popleft()
        if a[0] == 0:
            cur -= 1
            if i != m:
                info = [pizza[i]//2, i + 1]
                q.append(info)
                i += 1
        else:
            melting = [a[0]//2, a[1]]
            q.append(melting)
    return q[0][1]


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N : 화덕의 크기, M : 피자 개수
    Ci = list(map(int, input().split()))
    result = last_pizza(Ci, N, M)

    print(f"#{tc} {result}")