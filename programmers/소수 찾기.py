import math


def solution(n):
    answer = 0
    for i in range(2, n + 1, 1):
        IS_PRIME = True
        root_number = int(math.sqrt(i)) + 1
        for j in range(2, root_number, 1):
            if i % j == 0:
                IS_PRIME = False
                break
        if IS_PRIME:
            answer += 1

    return answer