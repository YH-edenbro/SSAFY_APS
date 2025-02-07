# 숫자를 정렬하자.

 # 카운팅 정렬렬
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    n_list = list(map(int, input().split()))

    count_list = [0] * (max(n_list) + 1)

    # 요소의 개수 세기
    for i in range(n):
        count_list[n_list[i]] += 1

    # 누적합 만들기
    for i in range(1, len(count_list)):
        count_list[i] = count_list[i] + count_list[i-1]

    # 정렬할 새로운 배열 TEMP생성 및 정렬 실행
    TEMP = [0] * n
    for i in range(n-1, -1, -1):
        count_list[n_list[i]] -= 1
        TEMP[count_list[n_list[i]]] = n_list[i]

    print(f"#{tc}", *TEMP)
