# SWEA min max 문제제

T = int(input())  # 테스트 케이스 개수 입력

for test_case in range(1, T+1):
    n = int(input())  # 양수의 개수 n 입력
    ai = list(map(int, input().split()))  # n개의 양수

    min_n = ai[0]
    max_n = ai[0]

    for i in range(1, n):
        if min_n > ai[i]:
            min_n = ai[i]
        elif max_n < ai[i]:
            max_n = ai[i]

    print(f'#{test_case} {max_n - min_n}')


# SWEA 구간합

T = int(input())

for test_case in range(1, T+1):

    n, m = map(int, input().split())
    ai = list(map(int, input().split()))

    m_list = []

    for i in range(n):
        if i + m > n:
            break
        m_list.append(ai[i:i+m])

    big_n = sum(m_list[0])
    small_n = sum(m_list[0])

    for item in m_list:          
        if big_n < sum(item):
            big_n = sum(item)
        elif small_n > sum(item):
            small_n = sum(item)

    print(f'#{test_case} {big_n - small_n}')


# View

for test_case in range(1, 11):
    n = int(input())
    height = list(map(int, input().split()))

    window = 0

    for i in range(2, n-2):
        if height[i] > height[i-2] and height[i] > height[i+2]:
            if height[i] > height[i+1] and height[i] > height[i-1]:
                window = window + height[i] - max(height[i+1], height[i+2], height[i-1], height[i-2])

    print(f'#{test_case} {window}')

# View 강사님 코드

for test_case in range(1, 11):
    n = int(input()) # 건물 개수
    buildings = list(map(int, input().split())) # 건물 높이 정보

    # 조망권 확보 세대 수
    total_view = 0
    # 첫 번째 검사 대상의 건물 인덱스
    # 왼쪽에서 2번째는 검사할 필요가 없다. 왼쪽 2칸이 확보 x

    i = 2 

    # 오른쪽 2칸 전까지 모든 건물의 조망권을 검사한다.
    while i < n-2:
        cnt_building_h = buildings[i]  # 현재 조망권 확인하려고 하는 건물의 높이
        left1, left2 = buildings[i - 1], buildings[i + 1] # 기준 건물의 왼쪽 2개 건물
        right1, right2 = buildings[i + 1], buildings[i + 2] # 기준 건물의 오른쪽 2개 건물

        max_h = max(left1, left2, right1, right2) # 좌우 총 4개 건물에서 가장 큰 높이를 가져온다.
        # 좌우 4개의 건물들의 최대 높이가 현재 건물보다 작으면
        # 그 차이만큼 조망권을 확보한다!
        if max_h < cnt_building_h:
            total_view += (cnt_building_h - max_h)
            i += 3 # 현재 건물이 조망권을 확보했다면 좌우 2개의 건물들은 조망권 확보가 불가능.
        # 그 외의 경우 (좌우 4개의 최대 높이가 현재 건물보다 같거나 높은 경우 -> 조망권 확보 x -> 다음 건물로)    
        else:
            i += 1



# Gravity

T = int(input())
 
for test_case in range(1, T+1):
    n = int(input()) # 가로의 길이
    box = list(map(int, input().split()))
 
    fall_count = 0 # 낙차
 
    # 각 위치별 쌓인 박스의 높이가 자신 보다 바로 뒤에 있는 박스 보다 높을 경우에 한칸씩 추가 되는 방식
    for i in range(n):
        fall_i = 0 #i에 위치한 박스의 낙차
        for j in range(i+1, n):
            if box[j] < box[i]:
                fall_i += 1
 
        # i에 위치한 박스의 낙차가 fall_count 보다 클 경우 fall_count 갱신
        if fall_count < fall_i:
            fall_count = fall_i
 
    print(f"#{test_case} {fall_count}")