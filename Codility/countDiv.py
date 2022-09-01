# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6


    ## 시간초과
    #divisible = 0
    # for i in range(A, B + 1, 1):
    #     if i % K == 0:
    #         divisible += 1
    #return divisible


    #Detected time complexity: O(1)
    count_A = A//K
    count_B = B//K

    if A%K==0:
        return count_B-count_A+1
    else:
        return count_B-count_A

