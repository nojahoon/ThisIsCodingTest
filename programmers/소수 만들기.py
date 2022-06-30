from itertools import combinations
import math


def solution(nums):
    arr_comb = []
    arr_prime = []

    # 조합 3개 선택
    for i in combinations(nums, 3):
        arr_comb.append(i)

    # 합산 수에 대해 소수판별
    for num in arr_comb:
        target = sum(num)
        judge = Is_prime(target)
        if judge:
            arr_prime.append(target)
    answer = len(arr_prime)

    return answer


def Is_prime(number):
    # number의 제곱근까지 판별하도록 설정
    for i in range(2, int(math.sqrt(number)) + 1, 1):
        if number % i == 0:
            return False
    return True
