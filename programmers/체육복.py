def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    #여분의 체육복을 소지한 사람이 도난당하였는지 조사
    for extra in reserve[:]:
        if extra in lost:
            lost.remove(extra)
            reserve.remove(extra)
    #다른사람에게 체육복을 줄 수 있는지 조사
    for extra in reserve[:]:
        #앞번호 조사
        if extra-1 in lost:
            lost.remove(extra-1)
        #뒷번호 조사
        elif extra+1 in lost:
            lost.remove(extra+1)

    answer = n - len(lost)

    return answer