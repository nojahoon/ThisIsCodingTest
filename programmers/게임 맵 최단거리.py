from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])

    queue = deque([[0, 0]])

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while queue:
        v = queue.popleft()
        x = v[0]
        y = v[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1:
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append([nx, ny])
    if maps[N - 1][M - 1] == 1:
        return -1
    else:
        return maps[N - 1][M - 1]