def solution(arr):
    arr.remove(min(arr))
    if arr:
        return arr
    else:
        return [-1]