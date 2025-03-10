# 스택(Stack)

## 스택(stack)의 특성
- 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조이다.
- 스택에 저장된 자료는 선형 구조를 갖는다.
  - 선형구조 : 자료 간의 관계가 1대1의 관계를 갖는다.
  - 비선형구조 : 자료 간의 관계가 1대N의 관계를 갖는다.(예 : 트리)
- 스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있다.
- 마지막에 삽입한 자료를 가장 먼저 꺼낸다.
- 후입선출(LIFO, Last-In-First-Out)이라고 부른다.
- 예를 들어 스택에 1,2,3 순으로 자료를 삽입한 후 꺼내면 역순으로 즉 3,2,1 순으로 꺼낼 수 있다.

## 스택의 구현
### 스택을 프로그램에서 구현하기 위해서 필요한 자료구조와 연산

- **자료구조** : 자료를 선형으로 저장할 저장소
  - 배열을 사용할 수 있다.
  - 저장소 자체를 스택이라 부르기도 한다.
  - 스택에서 마지막 삽입된 원소의 위치를 top이라 부른다.
- **연산**
  - 삽입: 저장소에 자료를 저장한다. 보통 push라고 부른다.
  - 삭제: 저장소에서 자료를 꺼낸다. 꺼낸 자료는 삽입한 자료의 역순으로 꺼낸다. 보통 pop이라고 부른다.
  - 스택이 공백인지 아닌지를 확인하는 연산. isEmpty
  - 스택의 top에 있는 item(원소)을 반환하는 연산. peek

```
- 스택의 push 알고리즘

def push(item):
    s.append(item)
```
```
스택의 push 구현

def push(item, size):
    global top
    top += 1
    if top==size:
        print('overflow!')
    else:
        stack[top] = item

size = 10
stack [0] * size
top = -1

push(10,size)

top += 1            # push(20)
stack[top] = 20     #
```
```
- 스택의 pop 알고리즘
def pop():
    if len(s) == 0:
        # underflow
        return
    else:
        return s.pop()
```
```
스택의 pop 구현

def pop():
    global top
    if top == -1:
        print('underflow')
        return 0
    else:
        top -= 1
        return stack[top+1]
print(pop())

if top > -1:    # pop()
    top -= 1
    print(stack[top+1])
```

## 스택 구현 고려 사항
- 1차원 배열을 사용하여 구현할 경우 구현이 용이하다는 장점이 있지만 스택의 크기를 변경하기가 어렵다는 단점이 있다.
- 이를 해결하기 위한 방법으로 저장소를 동적으로 할당하여 스택을 구현하는 방법이 있다. 동적 연결리스트를 이용하여 구현하는 방법을 의미한다. 구현이 복잡하다는 단점이 있지만 메모리를 효율적으로 사용한다는 장점을 가진다. 스택의 동적 구현은 생략한다.


## Memoization

```
#memo를 위한 배열을 할당하고, 모두 0으로 초기화 한다.
#memo[0]을 0으로 memo[1]는 1로 초기화 한다.

def fibo1(n):
    global memo
    if n >= 2 and momo[n] == 0:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1
```

## DP(Dynamic Programming)

- 동적 계획 (Dynamic Programming) 알고리즘은 그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘이다.
- 동적 계획 알고리즘은 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘이다.
  

## DFS(Depth First Search, 깊이우선탐색)
- 비선형구조인 그래프 구조는 그래프로 표현된 자료를 빠짐없이 검색하는 것이 중요함.
- 두 가지 방법
  - 깊이 우선 탐색(DFS)
  - 너비 우선 탐색(BFS)
  