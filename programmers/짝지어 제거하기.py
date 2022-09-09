def solution(s):
    stk = []
    for st in s:
        if len(stk) == 0:
            stk.append(st)
        else:
            if stk[-1] == st:
                stk.pop()
            else:
                stk.append(st)
    if len(stk) == 0:
        return 1
    else:
        return 0
    # 시간초과떠서 stack 쓰는 방향으로 전환
    # pre = 0
    # next = 1
    #
    # while len(s) >= 1 and next < len(s):
    #     if len(s) == 1:
    #         return 0
    #     if s[pre] == s[next]:
    #         if pre == 0:
    #             s = s[next+1:len(s)]
    #         else:
    #             s = s[0:pre] + s[next+1:len(s)]
    #         pre = 0
    #         next = 1
    #     else:
    #         pre += 1
    #         next += 1
    # if len(s) == 0:
    #     return 1
    # return 0