def solution(absolutes, signs):
    answer = 0

    if len(absolutes) != len(signs):
        return

    length = len(absolutes)

    for i in range(0, length, 1):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer