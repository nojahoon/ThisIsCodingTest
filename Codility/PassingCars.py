# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    zero = 0
    passing = 0
    for i in A:
        if i == 0:
            zero += 1
        else:
            passing += zero
    if passing > 1000000000:
        return -1
    return passing