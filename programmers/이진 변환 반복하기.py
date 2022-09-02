def solution(s):
    answer = []
    count = 0
    delete = 0
    while s!='1':
        n = s.count('1')
        delete += len(s)-n
        s = bin(n).lstrip('0b')
        count+=1
    return [count,delete]