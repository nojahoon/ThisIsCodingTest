def solution(s):
    answer = ''

    length = len(s)
    word_count = 0
    for i in range(length):
        if word_count % 2 == 0:
            answer += s[i].upper()
        else:
            answer += s[i].lower()
        if s[i] != ' ':
            word_count += 1
        else:
            word_count = 0
    return answer