import math
def solution(w,h):
    findgcd = math.gcd(w,h)
    return w * h - ( findgcd * ((w/findgcd) + (h/findgcd) - 1))
