def solution(s, n):
    answer = ''

    for alpha in s:
        if ord('a') <= ord(alpha) <= ord('z'):
            if ord(alpha) + n <= ord('z'):
                alpha = chr(ord(alpha) + n)
            else:
                alpha = chr((ord(alpha) + n) % 123 + 97)
            answer += alpha
        elif ord('A') <= ord(alpha) <= ord('Z'):
            if ord(alpha) + n <= ord('Z'):
                alpha = chr(ord(alpha) + n)
            else:
                alpha = chr((ord(alpha) + n) % 91 + 65)
            answer += alpha
        elif alpha == ' ':
            answer += ' '
    return answer