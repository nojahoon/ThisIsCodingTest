# FrogJmp
# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/

def solution(X, Y, D):
    # write your code in Python 3.6

    count = 0

    while (X < Y):
        X += D
        count += 1
    return count