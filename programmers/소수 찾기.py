from itertools import permutations

def solution(n):
    answer=0
    num = [i for i in n]
    per = []
    for i in range(1,len(num)+1):
        per+=list(permutations(num,i))
    num = [int(("").join(i)) for i in per]
    num = list(set(num)) #중복요소 제거
    for check_num in num:
        if check_num<2:
            continue
        for i in range(2,int(check_num**0.5)+1,1):
            if check_num%i==0:
                break
        else: #소수
            answer+=1
    return answer

print(solution("011"))