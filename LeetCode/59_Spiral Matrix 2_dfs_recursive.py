from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def dfs(matrix, x, y, count, IS_UP=False):
            if x < 0 or y < 0 or x > n - 1 or y > n - 1 or matrix[x][y] != 0:
                return
            if matrix[x][y] == 0:
                matrix[x][y] = count
                count += 1
                if not IS_UP or (IS_UP and x - 1 >= 0 and x - 1 < n - 1 and y >= 0 and y < n - 1 and matrix[x-1][y]!=0):
                    dfs(matrix, x, y + 1, count)
                dfs(matrix, x + 1, y, count)
                dfs(matrix, x, y - 1, count)
                dfs(matrix, x - 1, y, count, True)

        matrix = [[0] * n for _ in range(n)]
        count = 1
        dfs(matrix, 0, 0, count)
        return matrix