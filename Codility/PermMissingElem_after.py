# PermMissingElem
# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

def solution(A):
    length = len(A)
    if (length == 0):
        return 1
    else:
        return sum(range(1, len(A) + 2, 1)) - sum(A)