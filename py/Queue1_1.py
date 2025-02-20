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