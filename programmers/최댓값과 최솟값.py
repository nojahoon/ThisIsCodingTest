def solution(s):
    arr = list(map(int,s.split(' ')))
    answer=''
    answer += str(min(arr)) + ' '
    answer += str(max(arr))
    return answer