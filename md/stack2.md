# 백트래킹(Backtracking)

### - 백트래킹(Backtracking) 기법은 해를 찾는 도중에 '막히면' (즉, 해가 아니면) 되돌아가서 다시 해를 찾아 가는 기법이다.

### - 백트래킹 기법은 최적화(optimization) 문제와 결정(decision)문제를 해결할 수 있다.

### - 결정문제 : 문제의 조건을 만족하는 해가 존재하는지의 여부를 'yes'또는 'no'가 답하는 문제.
- 미로 찾기
- n-Queen 문제
- Map coloring
- 부분 집합의 합(Subset Sum)의 문제 등

## 백트래킹과 깊이우선탐색과의 차이
- 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄입. (Prunning 가지치기)

- 깊이우선탐색이 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단.

- 깊이우선탐색을 가하기에는 경우의 수가 너무나 많음. 즉, N! 가지의 경우의 수를 가진 문제에 대해 깊이우선탐색을 가하면 당연히 처리 불가능한 문제.

- 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수 시간(Exponential Time)을 요하므로 처리불가능

### 백트래킹은 모든 후보를 검사하지 않음.

### 백트래킹 기법
- 어떤 노드의 유망성을 점검한 후에 유망(promising)하지 않다고 결정되면 그 노드의 부모로 되돌아가(backtracking) 다음 자식 노드로 감

- 어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며, 반대로 해답의 가능성이 있으면 유망하다고 한다.

- 가지치기(pruning) : 유망하지 않는 노드가 포함되는 경로는 더 이상 고려하지 않는다.

### 백트래킹 알고리즘 절차
1. 상태 공간 트리의 깊이 우선 검색을 실시한다.

2. 각 노드가 유망한지를 점검한다.

3. 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속한다.


## 깊이 우선 검색 VS 백트래킹 ("DFS" -> 재귀 -> 백트래킹(가지치기))
- 순수한 깊이 우선 검색 = 155 노드
- 백트래킹 = 27 노드

## 순열


## 가지치기

- 가지치기를 잘 하면 연산이 빨라짐.