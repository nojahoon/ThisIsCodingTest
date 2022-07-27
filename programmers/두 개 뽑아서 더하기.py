from itertools import combinations

def solution(numbers):
    answer = []
    for i in combinations(numbers,2):
        if i[0]+i[1] not in answer:
            answer.append(i[0]+i[1])
    answer.sort()
    return answer