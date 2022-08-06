from collections import deque
def bfs(matrix,x,y):
    queue = deque([[x,y]])

    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    while queue:
        v = queue.popleft()
        x = v[0]
        y = v[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1 or matrix[nx][ny] == 0:
                continue
            if matrix[nx][ny]==1:
                matrix[nx][ny]=matrix[x][y]+1
                queue.append([nx,ny])
    return matrix[N-1][M-1]

N,M = map(int,input().split())
matrix = [list(map(int,input())) for _ in range(N)]
print(bfs(matrix,0,0))