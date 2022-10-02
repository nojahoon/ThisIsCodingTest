def solution(s):
    answer = 0
    for i in range(0, len(s), 1):
        stk = list(s[:])
        judge_stk = []
        for j in range(0, i, 1):
            parenthesis = stk.pop(0)
            stk.append(parenthesis)

        IS_RIGHT = True
        while stk:
            v = stk.pop(0)
            if v == '[' or v == '(' or v == '{':
                judge_stk.append(v)
            else:
                if not judge_stk:
                    IS_RIGHT = False
                    break
                else:
                    element = judge_stk.pop()
                    if element == '[' and v == ']':
                        continue
                    elif element == '(' and v == ')':
                        continue
                    elif element == '{' and v == '}':
                        continue
                    else:
                        IS_RIGHT = False
                        break
        if len(judge_stk) > 0 or IS_RIGHT == False:
            continue
        else:
            answer += 1
    return answer