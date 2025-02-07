# 2차원 배열

## 2차원 배열의 선언
- 1차원 List를 묶어놓은 List
- 2차원 이상의 다차원 List는 차원에 따라 Index를 선언
- 2차원 List의 선언 : 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
- Python에서는 데이터 초기화를 통해 변수선언과 초기화가 가능함

```
arr = [[0,1,2,3],[4,5,6,7]] (2행 4열의 2차원 List)
```

```
3
1 2 3     N = int(input())
4 5 6
7 8 9     arr = [list(map(int, input().split())) for _ in range(N)]
```

```
0으로 채워진 3*4 배열 만들기

arr = [[0] * 4 for _ in range(3)]

arr = [[0] * 4] * 3 - 하면 안됨. 각 행이 참조하는 주소가 같음.
 
```

### 델타 활용 탐색

di = [0, 1, 0, -1]   # 오른쪽부터 시계방향으로
dj = [1, 0, -1, 0]

```
N = 2
M = 3

i = 2
j = 3

for i in range(N):
    for j in range(M):
        for dr in range(4):
            ni = i + di[dr]
            nj = j + dj[dr]
            if 0 <= ni < N and 0 <= nj < M:
                print(ni, nj)
```

```
N = 2
M = 3

for i in range(N):
    for j in range(M):
        for di, dj in [[0, 1], [1, 0], [0,-1], [-1, 0]]:
            ni = i + dj
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M:
                print(ni, nj)
```
```
상하좌우 K칸의 합계 중 최대값

max_v = 0
for i in range(N):
    s = arr[i][j]
    for di, dj in [[0,1], [1, 0], [0, -1], [-1, 0]]:
        for c in range(1, k+1):
            ni, nj = i+di*c, j+dj*c
            if 0 <= ni < N and 0 <= nj < N:
                s += arr[ni][nj]
        if max_v < s:
            max_v = s

```
### 전치 행렬

```

```


### 비트 연산자 (같은 자리 비트끼리)

- & : 비트 단위로 AND 연산 
- | : 비트 단위로 OR 연산
- << : 피연산자의 비트 열을 왼쪽으로 이동시킨다.
- 　>> 피연산자의 비트 열을 오른쪽으로 이동시킨다. 