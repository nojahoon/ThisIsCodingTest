### BFS(Breadth-First Search)

- BFS는 너비 우선 탐색이라고도 불리며, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
- BFS는 큐 자료구조를 이용하며, 전체적인 동작 과정은 다음과 같다.
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리한다.
3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.

### BFS 동작 예시

- [Step 0] 그래프를 준비한다. (방문 기준: 번호가 낮은 인접 노드부터)
  + 시작 노드:1
  <img width="456" alt="0" src="https://user-images.githubusercontent.com/59651691/162892495-8e27f9a1-0d20-46ee-8f17-bcdb0c377b07.PNG">


- [Step 1] 시작 노드인 '1'을 큐에 삽입하고 방문 처리를 한다.

<img width="541" alt="1" src="https://user-images.githubusercontent.com/59651691/162892572-8ecbb707-7f3f-4342-b15c-a6955e86c403.PNG">

- [Step 2] 큐에서 노드 '1'을 꺼내 방문하지 않은 인접 노드 '2','3','8'을 큐에 삽입하고 방문 처리한다.

<img width="543" alt="2" src="https://user-images.githubusercontent.com/59651691/162892591-ea758dcc-51d5-41b0-b1a4-6760f8e9b693.PNG">


- [Step 3] 큐에서 노드 '2'를 꺼내 방문하지 않은 인접 노드 '7'을 큐에 삽입하고 방문 처리한다.

<img width="535" alt="3" src="https://user-images.githubusercontent.com/59651691/162892610-b789ba26-eff2-41ab-a3ce-6259c748e0c4.PNG">

- [Step 4] 큐에서 노드 '3'을 꺼내 방문하지 않은 인접 노드 '4','5'를 큐에 삽입하고 방문 처리한다.

<img width="536" alt="4" src="https://user-images.githubusercontent.com/59651691/162892622-31bd1913-bfc2-4c42-b5e4-c9996ab08a11.PNG">

- [Step 5] 큐에서 노드 '8'을 꺼내고 방문하지 않은 인접 노드가 없으므로 무시한다.

<img width="536" alt="5" src="https://user-images.githubusercontent.com/59651691/162892638-e60eb1f0-9660-42b7-9367-2916e9e23755.PNG">

- 이러한 과정을 반복하여 전체 노드의 탐색 순서(큐에 들어간 순서)는 다음과 같다.

<img width="546" alt="order" src="https://user-images.githubusercontent.com/59651691/162892663-918707a8-3d1f-4ed7-98d5-25af6b474842.PNG">


- 탐색 순서: 1 -> 2 -> 3 -> 8 -> 7 -> 4 -> 5 -> 6


- 간선의 길이가 동일한순서끼리부터 탐색 되는것을 확인할 수 있다. 

### BFS 소스코드 예제

```python
from collections import deque

# BFS 메서드 정의

def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue= deque([start])
    # 현재 노드르 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v,end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

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

#정의된 BFS 함수 호출
bfs(graph,1,visited)


```

```python
1 2 3 8 7 4 5 6
```
