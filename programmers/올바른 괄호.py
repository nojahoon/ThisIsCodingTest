def solution(s):
    stk = []
    for parenthesis in s:
        if parenthesis =='(':
            stk.append(parenthesis)
        else:
            if not stk:
                return False
            if stk[len(stk)-1]=='(':
                stk.pop()
            else:
                return False
    return True if not stk else False