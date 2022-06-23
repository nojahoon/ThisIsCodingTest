from itertools import permutations


def solution(numbers):
    str_arr = []  # str concatenate 후 integer로 바꾸기용 arr

    length = len(numbers)

    for i in permutations(numbers, length):
        str_arr.append("".join(map(str, i)))

    int_arr = [int(i) for i in str_arr]  # int형으로 만들기

    answer = str(max(int_arr))  # 문자열로 바꾸어 return

    return answer