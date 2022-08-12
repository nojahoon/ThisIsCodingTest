def solution(numbers, target):
    answer = 0
    n = len(numbers)

    def dfs(index, count):
        if index == n:
            if count == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(index + 1, count + numbers[index])
            dfs(index + 1, count - numbers[index])

    dfs(0, 0)
    return answer