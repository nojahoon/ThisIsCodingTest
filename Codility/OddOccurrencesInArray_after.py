# OddOccurrencesInArray
# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    length = len(A)
    A.sort()

    if length==0:
        return
    if length==1:
        return A[0]

    for i in range(0, length,2):
        if A[i] != A[i + 1]:
            return A[i]

    # 위의 for문 나오면 마지막 원소가 unpaired
    return A[length - 1]