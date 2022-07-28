from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        x = 0
        y = 0

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        direction = 0
        box = []
        answer = []

        for i in range(m):
            box.append(list(map(int, [0] * n)))

        answer.append(matrix[x][y])  # Initial
        box[0][0] = 1
        isEnd = False

        if m==1 and n==1:
            return answer

        while True:
            if isEnd == True:
                break
            nx = x + dx[direction]
            ny = y + dy[direction]

            if nx < 0 or ny < 0 or nx > m - 1 or ny > n - 1 or box[nx][ny]==1:
                direction = (direction + 1) % 4
                continue
            if box[nx][ny] == 0:
                answer.append(matrix[nx][ny])
                box[nx][ny] = 1
                x = nx
                y = ny
            isEnd=True
            for i in range(m):
                for j in range(n):
                    if box[i][j]==0:
                        isEnd = False
        return answer