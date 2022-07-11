def solution(numbers, hand):
    dic_x = {'1': 0, '2': 1, '3': 2,
             '4': 0, '5': 1, '6': 2,
             '7': 0, '8': 1, '9': 2,
             '*': 0, '0': 1, '#': 2}

    dic_y = {'1': 0, '2': 0, '3': 0,
             '4': 1, '5': 1, '6': 1,
             '7': 2, '8': 2, '9': 2,
             '*': 3, '0': 3, '#': 3}
    left = '*'
    right = '#'
    answer = ''
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            left = i
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            right = i
        else:
            judge_right = abs(dic_x[str(right)] - dic_x[str(i)]) + abs(dic_y[str(right)] - dic_y[str(i)])
            judge_left = abs(dic_x[str(left)] - dic_x[str(i)]) + abs(dic_y[str(left)] - dic_y[str(i)])
            if judge_right < judge_left:
                answer += 'R'
                right = i
            elif judge_right == judge_left:
                if hand == 'right':
                    right = i
                    answer += 'R'
                else:
                    left = i
                    answer += 'L'
            else:
                answer += 'L'
                left = i

    return answer