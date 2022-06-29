# TapeEquilibrium
# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

def solution(A):

    length=len(A)
    if length==2:
        return abs(A[0]-A[1])
    min=99999999999
    for i in range(length):
        count_forth=0
        count_back=0
        calculate=0
        #처음부터 P-1 까지
        for j in range(0,i+1,1):
            count_forth+=A[j]
        #P부터 N-1까지
        for k in range(i+1,length,1):
            count_back+=A[k]
        calculate = abs(count_forth-count_back)

        if calculate<min:
            min=calculate
    return min