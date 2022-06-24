def solution(answers):
    answer = []

    pattern_1 = [1, 2, 3, 4, 5]
    pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer_1 = 0
    answer_2 = 0
    answer_3 = 0

    length = len(answers)

    for i in range(length):
        index_1 = i % 5
        index_2 = i % 8
        index_3 = i % 10

        if pattern_1[index_1] == answers[i]:
            answer_1 += 1
        if pattern_2[index_2] == answers[i]:
            answer_2 += 1
        if pattern_3[index_3] == answers[i]:
            answer_3 += 1

    maximum = max(answer_1, answer_2, answer_3)

    if maximum == answer_1:
        answer.append(1)
    if maximum == answer_2:
        answer.append(2)
    if maximum == answer_3:
        answer.append(3)

    return answer