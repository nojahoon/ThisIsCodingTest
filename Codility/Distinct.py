# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    sett = set()
    for element in A:
        if element in sett:
            continue
        else:
            sett.add(element)
    return len(sett)