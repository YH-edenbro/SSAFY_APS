T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 신청서

    how_long = []
    dock_time = [0 for _ in range(25)]
    working_time = []

    for _ in range(N):
        s, e = map(int, input().split())  # s : 작업 시작 시간 , e : 종료시간
        work = (s, e, (e-s))
        working_time.append(work)

    # 인덱싱 정보 0: 시작시간, 1: 종료시간, 2: 걸리는 시간
    # 걸리는 시간이 짧은 순으로 정렬한다.
    for i in range(N-1, 0, -1):
        for j in range(i):
            if working_time[j][2] > working_time[j+1][2]:
                working_time[j], working_time[j+1] = working_time[j+1], working_time[j]

    cnt = 0  # 도크를 이용하는 트럭의 수
    for i in range(N):
        start = working_time[i][0]
        end = working_time[i][1]
        if dock_time[start] == 0:
            correct = 0
            for j in range(start, end):
                if dock_time[j] == 1:
                    break
                correct += 1
            if correct == (end - start):
                for j in range(start, end):
                    dock_time[j] = 1
                cnt += 1

    print(f"#{tc} {cnt}")
