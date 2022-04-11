### 그래프 탐색 알고리즘: DFS/BFS

- 탐색(Search)이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 말한다.
- 대표적인 그래프 탐색 알고리즘으로는 DFS와 BFS가 있다.
- DFS/BSF는 코딩 테스트에서 매우 자주 등장하는 유형이므로 반드시 숙지해야 한다.
- graph에 대해서 다루기 이전에 stack,queue,재귀 등에 대한 이해가 있어야 한다.

### 스택 자료구조

- 먼저 들어 온 데이터가 나중에 나가는 형식(선입후출)의 자료구조 : FILO(First In Last Out)
- 입구와 출구가 동일한 형태로 스택을 시각화할 수 있다.
- 박스쌓기예시

### 스택 구현 예제
- python에서 단순히 리스트 자료구조를 활용하면 된다.
- list 자료형은 가장 오른쪽에 원소를 삽입하는 append 함수와 가장 오른쪽 원소를 꺼내는 pop 함수를 지원하기에 stack 자료구조로 사용하기에 적합하다.
```python
stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)     
stack.pop()         #FILO 이므로 7 삭제
stack.append(1)
stack.append(4)
stack.pop()         #FILO 이므로 4 삭제

print(stack[::-1]) # 최상단 원소부터 출력
print(stack) #최하단 원소부터 출력

```
```
실행결과
[1,3,2,5]
[5,2,3,1]
```


### 큐 자료구조
- 먼저 들어 온 데이터가 먼저 나가는 형식(선입선출)의 자료구조 : FIFO(FIRST In First Out)
- 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 할 수 있다.
- 리스트 자료구조를 활용할수도있지만 시간복잡도를 고려할때 큐를 사용하는 것이 바람직하다. 
### 큐 구현 예제
```python
from collections import deque
# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) #먼저 들어온 순서대로 출력
queue.reverse() #역순으로 바꾸기
print(queue) #나중에 들어온 원소부터 출력

```
```python
실행결과
deque([3,7,1,4])
dqeue([4,1,7,3])
```

### 재귀 함수
- 재귀 함수(Recursive Function)란 자기 자신을 다시 호출하는 함수를 의미한다.
- 단순한 형태의 재귀 함수 예제
  + '재귀 함수를 호출합니다.'라는 문자열을 무한히 출력합니다.
  + 어느 정도 출력하다가 최대 재귀 깊이 메시지가 출력됩니다.
```python
def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()
recursive_function()

```

### 재귀 함수의 종료 조건
- 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야 한다.
- 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있다.
  + 종료 조건을 포함한 재귀 함수 예제
```python
def recursive_function(i):
    # 100번째 호출을 했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀함수에서' , i+1 , '번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀함수를 종료합니다.')
recursive_function(1)


```

### 팩토리얼 구현 예제
- n! = 1 x 2 x 3 x  ... x (n-1) x n
- 수학적으로 0!과 1!의 값은 1입니다.

```python
# 반복적으로 구현한 n!
def factorial_iterative(n):
  result=1
  #1부터 n까지의 수를 차례대로 곱하기
  for i in range(1,n+1):
    result *= i
  return result

# 재귀적으로 구현한 n!

def factorial_recursive(n):
  if n <= 1: n이 1 이하인 경우 1을 반환
    return 1
  # n! = n * (n-1)! 를 그대로 코드로 작성하기
  return n * factorial_recursive(n-1)

# 각각의 방식으로 구현한 n! 출력(n=5)
print('반복적으로 구현:',factorial_iterative(5))
print('재귀적으로 구현:',factorial_recursive(5))

```
```python
실행결과
반복적으로 구현: 120
재귀적으로 구현: 120

```

### 최대공약수 계산 (유클리드 호제법) 예제
- 두 개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘으로는 유클리드 호제법이 있다.
- 유클리드 호제법
  + 두 자연수 A,B에 대하여 (A>B) A를 B로 나눈 나머지를 R이라고 합시다.
  + 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다.
- 유클리드 호제법의 아이디어를 그대로 재귀 함수로 작성할 수 있다.
  + 예시: GCD(192,162)
  

| 단계  |  A  |  B  |
|:---:|:---:|:---:|
|  1  | 192 | 162 |
|  2  | 162 | 30  |
|  3  | 30  | 12  |
|  4  | 12  |  6  |

```python
def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b,a % b)
print(gcd(192,162))
```
```python
실행결과
6
```
### 재귀 함수 사용의 유의 사항
- 재귀 함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성할 수 있다.
  + 단, 오히려 다른 사람이 이해하기 어려운 형태의 코드가 될 수도 있으므로 신중하게 사용해야 한다.
- 모든 재귀 함수는 반복문을 이용하여 동일한 기능을 구현할 수 있다.
- 재귀 함수가 반복문보다 유리한 경우도 있고 불리한 경우도 있다.
- 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓인다.
  + 그래서 스택을 사용해야 할 때 구현상 스택 라이브러리 대신에 재귀 함수를 이용하는 경우가 많다.
