# PermCheck
# https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/

def solution(A):
    length = len(A)

    #중복여부 검사
    set_A = set(A)
    if len(set_A) != len(A):
        return 0

    for i in range(1, length+1, 1):
        if i not in set_A:
            return 0
    return 1
