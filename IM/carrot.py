T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
 
    max_s = 1  # 연속으로 커지는 당근의 최대 개수
    s = 1  # 연속 개수 기록(기본값 1)
    i = 0
    while i < N - 1:
        # 당근이 커지면 연속 개수 + 1
        if C[i+1] > C[i]:
            s += 1
         
        # 당근이 작아졌으면 지금까지 연속이었던 수와 최대 연속 수 비교
        # s 초기화
        if C[i+1] <= C[i]:
            max_s = max(max_s, s)
            s = 1
        i += 1
    max_s = max(max_s, s) # 최종 s와 max_s 비교해서 더 큰값
 
    print(f"#{tc} {max_s}")
