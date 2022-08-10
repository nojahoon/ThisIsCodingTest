def solution(n):
    answer=''
    while n>=1:
        remainder=n%3
        n=n//3
        answer+=str(remainder)
    return int(answer,3)