def solution(n):
    answer = []
    n = str(n)
    length = len(n)
    for i in range(length - 1, -1, -1):
        answer.append(int(n[i]))
    return answer