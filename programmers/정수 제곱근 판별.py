def solution(n):
    judge = n ** 0.5

    if judge == int(judge):
        return (judge + 1) ** 2
    else:
        return -1