## 최단 경로 문제

- 최단 경로 알고리즘은 가장 짧은 경로를 찾는 알고리즘을 의미합니다.
- 다양한 문제 상황
  + 한 지점에서 다른 한 지점까지의 최단 경로
  + 한 지점에서 다른 모든 지점까지의 최단 경로
  + 모든 지점에서 다른 모든 지점까지의 최단 경로
- 각 지점은 그래프에서 노드로 표현
- 지점 간 연결된 도로는 그래프에서 간선으로 표현
<img width="414" alt="최단 경로 문제" src="https://user-images.githubusercontent.com/59651691/190856500-eeb083fc-7e66-4f50-8182-6b8dd3bc553b.PNG">




## 다익스트라 최단 경로 알고리즘 개요
- 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산합니다.
- 다익스트라 최단 경로 알고리즘은 음의 간선이 없을 때 정상적으로 동작합니다.
  + 현실 세계의 도로(간선)은 음의 간선으로 표현되지 않습니다.
- 다익스트라 최단 경로 알고리즘은 그리디 알고리즘으로 분류됩니다.
  + 매 상황에서 가장 비용이 적은 노드를 선택해 임의의 과정을 반복합니다.

- 알고리즘의 동작 과정은 다음과 같습니다.
  1. 출발 노드를 설정합니다.
  2. 최단 거리 테이블을 초기화합니다.
  3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택합니다.
  4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신합니다.
  5. 위 과정에서 3번과 4번을 반복합니다.
  

    
- 알고리즘 동작 과정에서 최단 거리 테이블은 각 노드에 대한 현재까지의 최단 거리 정보를 가지고 있습니다.
- 처리 과정에서 더 짧은 경로를 찾으면 '이제부터는 이 경로가 짧은 경로야.'라고 갱신합니다.
<img width="317" alt="다익스트라 최단 경로 알고리즘" src="https://user-images.githubusercontent.com/59651691/190856524-0d2e1218-f449-46a6-858f-bb5792b49ef9.PNG">

<img width="323" alt="최단 경로 알고리즘2" src="https://user-images.githubusercontent.com/59651691/190856527-c50e6546-206b-49e3-ab17-15c2b8122c17.PNG">




## 다익스트라 알고리즘 : 동작과정 살펴보기


- [초기 상태] 그래프를 준비하고 출발 노드를 설정합니다.    

<img width="708" alt="초기 상태" src="https://user-images.githubusercontent.com/59651691/190856550-905f6c3c-632c-45c4-8d57-623a846f9502.PNG">  



- [Step 1] 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드인 1번 노드를 처리합니다.    

<img width="849" alt="Step1" src="https://user-images.githubusercontent.com/59651691/190856555-fee4ec25-95e5-4d37-bd2d-d27b7b2e0a2b.PNG">  



- [Step 2] 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드인 4번 노드를 처리합니다.    

<img width="849" alt="Step 2" src="https://user-images.githubusercontent.com/59651691/190856562-b767704f-648a-4351-9f2d-dbeda72bbc15.PNG">  



- [Step 3] 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드인 2번 노드를 처리합니다.    

<img width="849" alt="step 3" src="https://user-images.githubusercontent.com/59651691/190856574-2c99f60b-f7bd-406c-8b9c-01ff77267014.PNG">  



- [Step 4] 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드인 5번 노드를 처리합니다.    

<img width="846" alt="Step 4" src="https://user-images.githubusercontent.com/59651691/190856581-95fb99b1-ecc3-46ca-a95c-18e0c7687590.PNG"> 


  
- [Step 5] 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드인 3번 노드를 처리합니다.    

<img width="849" alt="Step 5" src="https://user-images.githubusercontent.com/59651691/190856585-932c3e7a-72ed-499b-aea2-cf604f9536e2.PNG">  



- [Step 6] 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드인 6번 노드를 처리합니다.    

<img width="849" alt="step 6" src="https://user-images.githubusercontent.com/59651691/190856589-96e2a67c-d1e8-45f9-9e8a-0aa4f59887ee.PNG">  




## 다익스트라 알고리즘의 특징

- 그리디 알고리즘 : 매 상황에서 방문하지 않은 가장 비용이 적은 노드를 선택해 임의의 과정을 반복합니다.
- 단계를 거치며 한 번 처리된 노드의 최단 거리는 고정되어 더 이상 바뀌지 않습니다.
  + 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해할 수 있습니다.
- 다익스트라 알고리즘을 수행한 뒤에 테이블에 각 노드까지의 최단 거리 정보가 저장됩니다.
  + 완벽한 형태의 최단 경로를 구하려면 소스코드에 추가적인 기능을 더 넣어야 합니다.


## 다익스트라 알고리즘: 간단한 구현 방법
- 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 테이블의 모든 원소를 확인(순차 탐색)합니다.


``` python
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n,m = map(int,input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n +1)
# 최단 거리 테이블을 모드 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
  min_value = INF
  index = 0  # 가장 최단 거리가 짧은 노드(인덱스)
  for i in range(1,n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
   return index
 
def dijkstra(start):
  # 시작 노드에 대해서 초기화
  distance[start] = 0
  visited[start] = True
  for j in graph[start]:
    distance[j[0]] = j[1]
  # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
  
  for i in graph(n-1):
    # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
    now = get_smallest_node()
    visited[now] = True
    # 현재 노드와 연결된 다른 노드를 확인
    for j in graph[now]:
      cost = distance[now] + j[1]
      #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[j[0]]:
        distance[j[0]] = cost

#다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1,n+1):
  # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
  if distance[i]==INF:
    print("INFINITY")
  # 도달할 수 있는 경우 거리를 출력
  else:
  print(distance[i])
  
```


## 다익스트라 알고리즘: 간단한 구현 방법 성능 분석

- 총 O(V)번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색해야 합니다.
- 따라서 전체 시간 복잡도는 O(V^2)입니다.
- 일반적으로 코딩 테스트의 최단 경로 문제에서 전체 노드의 개수가 5,000개 이하라면 이 코드로 문제를 해결할 수 있습니다.
  + 하지만 노드의 개수가 10,000개를 넘어가는 문제라면 어떻게 해야 할까요?

## 우선순위 큐(Priority Queue)
- 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조입니다.
- 예를 들어 여러 개의 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건 데이터부터 꺼내서 확인해야하는 경우에 우선순위 큐를 이용할 수 있습니다.
- Python, C++, Java를 포함한 대부분의 프로그래밍 언어에서 표준 라이브러리 형태로 지원합니다.

| 자료구조                   | 추출되는 데이터        |
|------------------------|-----------------|
| 스택(Stack)              | 가장 나중에 삽입된 데이터  |
| 큐(Queue)               | 가장 먼저 삽입된 데이터   |
| 우선순위 큐(Priority Queue) | 가장 우선순위가 높은 데이터 |



## 힙(Heap)

- 우선순위 큐(Priority Queue)를 구현하기 위해 사용하는 자료구조 중 하나입니다.
- 최소 힙(Min Heap)과 최대 힙(Max Heap)이 있습니다.
- 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 사용됩니다.


| 우선순위 큐 구현 방식 |삽입 시간|삭제 시간|
|--------|---------------|----------|
| 리스트    | O(1) |O(N)|
| 힙(Heap) | O(logN) | O(log N)|


## 힙 라이브러리 사용 예제 : 최소 힙

```python
import heapq

# 오름차순 힙 정렬(Heap Sort)
def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h,value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for i in range(len(h)):
    result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

## 실행 결과 ##
[0,1,2,3,4,5,6,7,8,9]

```

## 힙 라이브러리 사용 예제: 최대 힙
```python
import  heapq

# 내림차순 힙 정렬(Heap Sort)
def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h,-value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for i in range(len(h)):
    result.append(-heapq.heappop(h))
  return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

## 실행 결과 ##
[9,8,7,6,5,5,4,3,2,1,0]

```

## 다익스트라 알고리즘 : 개선된 구현 방법
- 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 힙(Heap) 자료구조를 이용합니다.
- 다익스트라 알고리즘이 동작하는 기본 원리는 동일합니다.
  + 현재 가장 가까운 노드를 저장해 놓기 위해서 힙 자료구조를 추가적으로 이용한다는 점이 다릅니다.
  + 현재의 최단 거리가 가장 짧은 노드를 선택해야 하므로 쵝소 힙을 사용합니다.


## 다익스트라 알고리즘: 동작 과정 살펴보기 (우선순위 큐)

- [초기 상태] 그래프를 준비하고 출발 노드를 설정하여 우선순위 큐에 삽입합니다.

<img width="705" alt="초기 상태" src="https://user-images.githubusercontent.com/59651691/190910575-9692aa0c-872b-4fba-b212-15acbab1c6bd.PNG">


- [Step 1] 우선순위 큐에서 원소를 꺼냅니다. 1번 노드는 아직 방문하지 않았으므로 이를 처리합니다.

<img width="885" alt="Step1" src="https://user-images.githubusercontent.com/59651691/190910579-d21c81cd-645e-4be8-84ee-eeeab83761e5.PNG">


- [Step 2] 우선순위 큐에서 원소를 꺼냅니다. 4번 노드는 아직 방문하지 않았으므로 이를 처리합니다.

<img width="883" alt="Step2" src="https://user-images.githubusercontent.com/59651691/190910581-7b2b1d02-607a-47d8-9469-f9bc9eac9169.PNG">


- [Step 3] 우선순위 큐에서 원소를 꺼냅니다. 2번 노드는 아직 방문하지 않았으므로 이를 처리합니다.

<img width="886" alt="Step3" src="https://user-images.githubusercontent.com/59651691/190910585-3a244e4b-466d-43fa-b55d-8ce8b57b6eb4.PNG">


- [Step 4] 우선순위 큐에서 원소를 꺼냅니다. 5번 노드는 아직 방문하지 않았으므로 이를 처리합니다.

<img width="886" alt="Step4" src="https://user-images.githubusercontent.com/59651691/190910587-c69977c4-f2fb-4ad5-8303-6db65427636b.PNG">


- [Step 5] 우선순위 큐에서 원소를 꺼냅니다. 3번 노드는 아직 방문하지 않았으므로 이를 처리합니다.

<img width="884" alt="Step5" src="https://user-images.githubusercontent.com/59651691/190910589-5b54870b-a387-46f5-bb6f-f1938f0c174d.PNG">


- [Step 6] 우선순위 큐에서 원소를 꺼냅니다. 3번 노드는 이미 방문했으므로 무시합니다.

<img width="670" alt="Step6" src="https://user-images.githubusercontent.com/59651691/190910592-fdb88820-6621-4ecc-ad7f-70fd67aca795.PNG">


- [Step 7] 우선순위 큐에서 원소를 꺼냅니다. 6번 노드는 아직 방문하지 않았으므로 이를 처리합니다.

<img width="886" alt="Step7" src="https://user-images.githubusercontent.com/59651691/190910595-f84d45e9-3cff-44c2-9358-26dc5c40500f.PNG">


- [Step 8] 우선순위 큐에서 원소를 꺼냅니다. 3번 노드는 이미 방문했으므로 무시합니다.

<img width="666" alt="Step8" src="https://user-images.githubusercontent.com/59651691/190910597-13ebe5c6-07d0-4f26-add0-2979c026ac4a.PNG">


```python
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n,m = map(int,input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n +1)
# 최단 거리 테이블을 모드 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))
  

def dijkstra(start):
  q = []
  # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
  heapq.heappush(q, (0,start))
  distance[start] = 0
  while q: #큐가 비어있지 않다면
    # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
    dist , now = heapq.heappop(q)
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
    if distance[now] < dist:
      continue
    # 현재 노드와 연결된 다른 인접한 노드들을 확인
    for i in graph[now]:
      cost = dist + i[1]
      # 현재 노드를 고쳐서, 다른 노드로 이도앟는 거리가 더 짧은 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1,n+1):
  # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
  if distance[i]==INF:
    print("INFINITY")
  # 도달할 수 있는 경우 거리를 출력
  else:
    print(distance[i])
```

## 다익스트라 알고리즘:개선된 구현 방법 성능 분석
- 힙 자료구조를 이용하는 다익스트라 알고리즘의 시간 복잡도는 O(ElogV)입니다.
- 노드를 하나씩 꺼내 검사하는 반복문(while문)은 노드의 개수 V 이상의 횟수로는 처리되지 않습니다.
  + 결과적으로 현재 우선순위 큐에서 꺼낸 노드와 연결된 다른 노드들을 확인하는 총횟수는 최대 간선의 개수(E)만큼 연산이 수행될 수 있습니다.
- 직관적으로 전체 과정은 E개의 원소를 우선순위 큐에 넣었다가 모두 빼내는 연산과 매우 유사합니다.
  + 시간 복잡도를 O(ElogE)로 판단할 수 있습니다.
  + 중복 간선을 포함하지 않는 경우에 이를 O(ElogV)로 정리할 수 있습니다.
    * O(ElogE) -> O(ElogV^2)-> O(2ElogV) -> O(ElogV)


## 플로이드 워셜 알고리즘 개요

- 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산합니다.
- 플로이드 워셜(Floyd-Warshall)알고리즘은 다익스트라 알고리즘과 마찬가지로 단계별로 거쳐 가는 노드를 기준으로 알고리즘을 수행합니다.
  + 다만 매 단계마다 방문하지 않은 노드 중에 최단 거리를 갖는 노드를 찾는 과정이 필요하지 않습니다.
- 플로이드 워셜은 2차원 테이블에 최단 거리 정보를 저장합니다.
- 플로이드 워셜 알고리즘은 다이나믹 프로그래밍 유형에 속합니다.

## 플로이드 워셜 알고리즘
- 각 단계마다 특정한 노드 k를 거쳐 가는 경우를 확인합니다.
  + a에서 b로 가는 최단 거리보다 a에서 k를 거쳐 b로 가는 거리가 더 짧은지 검사합니다.
- 점화식은 다음과 같습니다.
<img width="254" alt="점화식" src="https://user-images.githubusercontent.com/59651691/191046149-e562d7aa-b504-4cd6-b70f-7d98c59b5d13.PNG">


## 플로이드 워셜 알고리즘: 동작 과정 살펴보기

- [초기 상태] 그래프를 준비하고 최단 거리 테이블을 초기화합니다.  

<img width="710" alt="초기상태" src="https://user-images.githubusercontent.com/59651691/191046177-a2a07257-4428-405a-a358-ca1eb51d903f.PNG">

- [Step 1] 1번 노드를 거쳐 가는 경우를 고려하여 테이블을 갱신합니다.

<img width="873" alt="Step1" src="https://user-images.githubusercontent.com/59651691/191046218-e5385299-da75-43de-b69f-d044d081e57a.PNG">


- [Step 2] 2번 노드를 거쳐 가는 경우를 고려하여 테이블을 갱신합니다.

<img width="864" alt="Step2" src="https://user-images.githubusercontent.com/59651691/191046253-f8f51ceb-0cc0-4477-9041-5bfcc04e3726.PNG">


- [Step 3] 3번 노드를 거쳐 가는 경우를 고려하여 테이블을 갱신합니다.

<img width="869" alt="Step3" src="https://user-images.githubusercontent.com/59651691/191046282-1bd90153-794e-4248-850b-9a1570847438.PNG">


- [Step 4] 4번 노드를 거쳐 가는 경우를 고려하여 테이블을 갱신합니다.

<img width="870" alt="Step4" src="https://user-images.githubusercontent.com/59651691/191046296-88dc8979-dc7d-4449-963b-8a7b06170b4f.PNG">


```python
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1,n+1):
  for b in range(1,n+1):
    if a==b:
      graph[a][b]=0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
  # A에서 B로 가는 비용은 C라고 설정
  a,b,c = map(int,input().split())
  graph[a][b]=c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b] , graph[a][k] + graph[k][b])
      
# 수행된 결과를 출력
for a in range(1,n+1):
  for b in range(1,n+1):
    # 도달할 수 없는 경우 무한(INFINITY)라고 출력
    if graph[a][b]==INF:
      print("INFINITY",end="")
    # 도달할 수 있는 경우 거리를 출력
    else:
      print(graph[a][b],end="")
  print()

```

## 플로이드 워셜 알고리즘 성능 분석
- 노드의 개수가 N개일 때 알고리즘상으로 N번의 단계를 수행합니다.
  + 각 단계마다 O(N^2)의 연산을 통해 현재 노드를 거쳐 가는 모든 경로를 고려합니다.
- 따라서 플로이드 워셜 알고리즘의 총 시간 복잡도는 O(N^3)입니다.

