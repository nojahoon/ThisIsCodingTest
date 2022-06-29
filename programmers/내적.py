def solution(a, b):
    if len(a) != len(b):
        return

    answer = 0
    length = len(a)
    for i in range(length):
        answer += a[i] * b[i]

    return answer