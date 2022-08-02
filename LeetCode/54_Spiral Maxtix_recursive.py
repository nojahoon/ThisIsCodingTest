from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def recursive_solution(matrix, start_x, start_y, answer_arr, check_arr):
            x = start_x
            y = start_y
            # recursion 시작부분은 바로 추가
            if x >= 0 and y >= 0 and x <= N - 1 and y <= M - 1 and check_arr[x][y] == 0:
                answer_arr.append(matrix[x][y])
                check_arr[x][y] = 1
            else:
                return
            dx = [0, 1, 0, -1]
            dy = [1, 0, -1, 0]
            i = 0
            while (True):
                if i == 4: break

                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1:
                    i += 1
                    continue
                if check_arr[nx][ny] != 0:
                    i += 1
                    continue
                if check_arr[nx][ny] == 0:
                    check_arr[nx][ny] = 1
                    answer_arr.append(matrix[nx][ny])
                    x = nx
                    y = ny
            nx = x + 0
            ny = y + 1
            if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1:
                return
            else:
                recursive_solution(matrix, nx, ny, answer_arr, check_arr)
        N = len(matrix)
        M = len(matrix[0])
        answer_arr = []
        check_arr = [[0] * M for _ in range(N)]

        recursive_solution(matrix, 0, 0, answer_arr, check_arr)
        return answer_arr
S = Solution()
print(S.spiralOrder([[1]]))