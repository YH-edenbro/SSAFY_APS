# 등산로 조성

import sys
sys.stdin = open("", "r")



T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    map_info = [list(map(int, input().split())) for _ in range(N)]


    def dfs(before_idx, k):
        dx = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        k_cnt = 0
        road_cnt = 0
        after_idx = []

        if map_info[after_idx[0]][after_idx[1]] < map_info[before_idx[0]][before_idx[1]]:
            return road_cnt

    # 2차원 배열에서 최대 값 찾기
    def find_max(arr):
        max_num = 0
        for i in range(N):
            for j in range(N):
                if arr[i][j] > max_num:
                    max_num = arr[i][j]
        return max_num

    top = find_max(map_info)

    long_road = 0
    for i in range(N):
        for j in range(N):
            if map_info[i][j] == top:
                start = [i, j]

    print(f"{tc}")