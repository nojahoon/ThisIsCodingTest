# PermMissingElem
# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

def solution(A):
    count = 1
    index = len(A)

    for i in range(1, index + 1, 1):
        if i in A:
            continue
        else:
            return i