def solution(begin, end):
    answer = []

    for i in range(begin, end + 1):
        if i == 1:
            answer.append(0)
            continue
        for j in range(2, int(i**0.5)+1):
            if i % j == 0 and i//j <=10**7:
                answer.append(i//j)
                break
        else:
            answer.append(1)
    return answer