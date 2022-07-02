def solution(a, b):
    if a==b:
        return a

    return sum(range(min(a,b),max(a,b)+1))