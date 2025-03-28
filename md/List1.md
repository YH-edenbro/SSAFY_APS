# APS(Algorithm Problem Solving) - 기본학습
- 입출력을 제외한 내장함수 사용하지 않기.
- 기본적인 내장함수의 동작원리 이해

# 알고리즘
- 알고리즘 : 유한한 단계를 통해 문제를 해결하기 위한 절차나 방법이다. 주로 컴퓨터용어로 쓰이며, 컴퓨터가 어떤 일을 수행하기 위한 단계적 방법을 말한다.
- 간단하게 다시 말하면 어떠한 문제를 해결하기 위한 절차라고 볼 수 있다.
- 예를 들어 1부터 100까지의 합을 구하는 문제를 생각해 보자.
- 컴퓨터 분야에서 알고리즘을 표현 하는 방법은 크게 두 가지.
  - 의사코드(슈도코드, Pseudocode)와 순서도
  
### 알고리즘의 성능

- APS 과정의 목표 중의 하나는 보다 좋은 알고리즘을 이해하고 활용하는 것이다.

- 무엇이 좋은 알고리즘인가?
    1. 정확성 : 얼마나 정확하게 동작하는가
    2. 작업량 : 얼마나 적은 연산으로 원하는 결과를 얻어내는가
    3. 메모리 사용량 : 얼마나 적은 메모리를 사용하는가
    4. 단순성 : 얼마나 단순한가
    5. 최적성 : 더 이상 개선할 여지없이 최적화되었는가
   
### 시간 복잡도 - 빅-오(O) 표기법



```
for _ in range(n): # 단순 반복 n회

```


### 안정성과 적응성

- 안정성 : 동일한 키가 있을때, 상대적 순서가 보존되는가
  - ex) [1, 6, 5, 4, 4, 2, 3] - 정렬하더라도 4끼리는 상대적 순서가 보존되어야 한다.
- 적응성 : 초기 정렬 상태에 따라서 실행 시간이 바뀌는지.
  - (ex: [6, 3, 1, 2, 4] vs [1, 3, 5, 4, 7])

### 제자리 정렬
- 외부 메모리를 사용했는가
  (버블정렬 : 제자리 정렬 o)
  (카운팅정렬 : 제자리 정렬 x)