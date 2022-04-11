### DFS (Depth-First Search)

- DFS는 깊이 우선 탐색이라고도 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
- DFS는 스택 자료구조(혹은 재귀 함수)를 이용하며, 구체적인 동작 과정은 다음과 같다.
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.

### DFS 동작 예시

- [Step 0] 그래프를 준비 ( 방문 기준: 번호가 낮은 인접 노드부터)

  - 시작 노드 : 1
<img width="453" alt="0" src="https://user-images.githubusercontent.com/59651691/162696723-f22be7c4-e55f-420e-bd47-f1b24c07345b.PNG">


- [Step 1] 시작 노드인 '1'을 스택에 삽입하고 방문 처리를 한다.
 <img width="547" alt="1" src="https://user-images.githubusercontent.com/59651691/162696770-877e945f-466f-474e-9631-a7c1cfd5442d.PNG">


- [Step 2] 스택의 최상단 노드인 '1'에 방문하지 않은 인접 노드 '2','3','8'이 있다.
  - 이중에서 가장 작은 노드인 '2'를 스택에 넣고 방문 처리를 한다.
<img width="542" alt="2" src="https://user-images.githubusercontent.com/59651691/162696908-92e28fc0-e5a8-4424-917d-1a34721881b1.PNG">

- [Step 3] 스택의 최상단 노드인 '2'에 방문하지 않은 인접 노드 '7'이 있다.
  - 따라서 '7'번 노드를 스택에 넣고 방문 처리를 한다.

<img width="536" alt="3" src="https://user-images.githubusercontent.com/59651691/162696931-72df99c2-fdb4-4a61-8389-da008e969074.PNG">

- [Step 4] 스택의 최상단 노드인 '7'에 방문하지 않은 인접 노드 '6','8'이 있다.
  - 이 중에서 가장 작은 노드인 '6'을 스택에 넣고 방문 처리를 한다.
<img width="533" alt="4" src="https://user-images.githubusercontent.com/59651691/162696956-9066273b-1b0e-48fa-8dfb-fbcd14d5da14.PNG">

- [Step 5] 스택의 최상단 노드인 '6'에 방문하지 않은 인접 노드가 없다.
  - 따라서 스택에서 '6'번 노드를 꺼낸다.
<img width="542" alt="5" src="https://user-images.githubusercontent.com/59651691/162696986-5f4f9dfb-03f7-4405-b18c-1ba1a9ba17d3.PNG">

- [Step 6] 스택의 최상단 노드인 '7'에 방문하지 않은 인접 노드 '8'이 있다.
  - 따라서 '8'번 노드를 스택에 넣고 방문 처리를 한다.
<img width="518" alt="6" src="https://user-images.githubusercontent.com/59651691/162697003-532849ad-7e5d-4c06-83e7-1e21321d1c87.PNG">

- 이러한 과정을 반복하였을 때 전체 노드의 탐색 순서(스택에 들어간 순서)는 다음과 같다.

<img width="487" alt="order" src="https://user-images.githubusercontent.com/59651691/162697022-2a28ac86-900d-4398-b7aa-eed01d24d172.PNG">

탐색 순서: 1 -> 2 -> 7 -> 6 -> 8 -> 3 -> 4 -> 5

- 최대한 깊게 가는 방식이기에 stack대신 재귀함수를 사용할 수 있다.

### DFS 소스코드 예제

```python
# DFS 메서드 정의
def dfs(graph, v , visited):
  #현재 노드를 방문 처리
  visited[v] = True
  print(v,end=' ')
  #현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

#각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph,1,visited)

```

```python
실행결과
1 2 7 6 8 3 4 5
```
