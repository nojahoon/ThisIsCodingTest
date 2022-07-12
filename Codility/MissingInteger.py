# MissingInteger
# https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/

def solution(A):

    A.sort()
    min_var=1
    length=len(A)
    for i in A:
        if i==min_var:
            min_var+=1
    return min_var