DATA = [0, 4, 1, 3, 1, 2, 4, 1]
N = len(DATA)

COUNTS = [0] * 5  # max(DATA) + 1
TEMP = [0] * N  # 원본의 크기와 같아야 함.

for i in range(N):
    COUNTS[DATA[i]] += 1

for i in range(1, 5):
    COUNTS[i] = COUNTS[i] + COUNTS[i-1]

for i in range(N-1, -1, -1):
    COUNTS[DATA[i]] -= 1  # DATA[i] 까지의 개수 1개 감소
    # DATA[i]까지 차지한 칸 수 중 가장 오른쪽에 DATA[i] 기록
    TEMP[COUNTS[DATA[i]]] = DATA[i]

print(DATA)
print(TEMP)
