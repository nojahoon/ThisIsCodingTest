from collections import deque

M,N = map(int,input().split(' '))
box = list()
for i in range(N):
    box.append(list(map(int,input().split(' '))))

queue = deque()

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append([j,i])

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(queue):
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>M-1 or ny>N-1:
                continue
            if box[ny][nx]==-1:
                continue
            if box[ny][nx]==0:
                box[ny][nx]= box[y][x] +1
                queue.append([nx,ny])
    for i in range(N):
        for j in range(M):
            if box[i][j]==0:
                return -1

    max = 0
    for i in range(N):
        for j in range(M):
            if box[i][j]>max:
                max=box[i][j]
    return max-1

print(bfs(queue))