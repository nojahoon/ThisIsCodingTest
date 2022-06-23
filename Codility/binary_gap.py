# BinaryGAP
# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

def solution(N):
    arr = bin(N).split('0b')[1]

    count = 0
    max = 0

    for number in arr:
        if number == '1':
            if max < count:
                max = count
            count = 0
        else:
            count += 1

    return max