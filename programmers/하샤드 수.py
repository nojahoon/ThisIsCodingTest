def solution(x):
    n = str(x)
    divisor=0
    for number in n:
        divisor+=int(number)
    if int(x)%divisor==0:
        return True
    return False