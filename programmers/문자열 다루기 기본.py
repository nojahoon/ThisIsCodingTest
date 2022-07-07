def solution(s):
    if len(s)!=4 and len(s)!=6:
        return False
    if str.isdigit(s):
        return True
    return False