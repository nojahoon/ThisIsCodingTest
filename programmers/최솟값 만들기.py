def solution(A, B):
    answer = 0

    if len(A) != len(B):
        return

    A.sort()
    B.sort()

    while A and B:
        answer += A.pop(0) * B.pop()

    return answer