def solution(s):
    s = s.lower()
    count_p = 0
    count_y = 0

    for string in s:
        if string == 'p':
            count_p += 1
        elif string == 'y':
            count_y += 1
    return True if count_p == count_y else False

# 아주 간결하게 하려면.. 이런방법도 있다고한다..
# return s.lower().count('p') == s.lower().count('y')