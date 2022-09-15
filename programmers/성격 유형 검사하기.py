def solution(survey, choices):
    answer = ""
    dic = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for i, choice in enumerate(choices):
        if choice == 4:
            continue
        elif 1 <= choice <= 3:
            if choice == 1:
                dic[survey[i][0]] += 3
            elif choice == 2:
                dic[survey[i][0]] += 2
            else:
                dic[survey[i][0]] += 1
        else:
            if choice == 5:
                dic[survey[i][1]] += 1
            elif choice == 6:
                dic[survey[i][1]] += 2
            else:
                dic[survey[i][1]] += 3

    answer += judgeChar('R', 'T', dic)
    answer += judgeChar('C', 'F', dic)
    answer += judgeChar('J', 'M', dic)
    answer += judgeChar('A', 'N', dic)
    return answer


def judgeChar(char1, char2, dic):
    if dic[char1] < dic[char2]:
        return char2
    elif dic[char1] > dic[char2]:
        return char1
    else:
        return char1 if char1 < char2 else char2

