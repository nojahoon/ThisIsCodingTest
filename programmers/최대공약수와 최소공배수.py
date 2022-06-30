def solution(n, m):
    answer = []

    answer.append(Find_GCF(n, m))
    answer.append(Find_LCM(n, m))

    return answer


def Find_GCF(n, m):  # Greatest Common Factor
    while (m):
        n, m = m, n % m
    return n


def Find_LCM(n, m):  #:Least Common Multiple
    return n * m // (Find_GCF(n, m))