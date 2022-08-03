def solution(dartResult):
    dict = {'S': 1, 'D': 2, 'T': 3}

    dartResult = dartResult.replace('10', 'X')
    stack = []

    for i in range(len(dartResult)):
        if dartResult[i].isdigit() or dartResult[i] == 'X':
            if dartResult[i] == 'X':
                stack.append(10)
            else:
                stack.append(int(dartResult[i]))
        else:
            if dartResult[i] in dict:
                num = stack.pop()
                stack.append(num ** dict[dartResult[i]])
            elif dartResult[i] == '*':
                num = stack.pop()
                if stack:
                    stack[-1] = stack[-1] * 2
                stack.append(num * 2)
            elif dartResult[i] == '#':
                stack[-1] *= -1
    return sum(stack)