# TapeEquilibrium
# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

# sum 계산해주는 부분의 로직을 수정하면 O(n^2)을 O(n)으로 줄일 수 있다.
def solution(A):

    sum_left = 0
    sum_right = sum(A)

    min = 9999999
    length = len(A)

    for i in range(0, length - 1, 1):
        sum_left += A[i]
        sum_right -= A[i]

        judge = abs(sum_left - sum_right)
        if judge < min:
            min = judge

    return min