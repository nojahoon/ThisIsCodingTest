def solution(numbers):
    str_arr = [str(num) for num in numbers]
    str_arr.sort(key=lambda num: num * 3, reverse=True)

    str_arr = "".join(str_arr)

    if int(str_arr) == 0:
        return '0'
    return str_arr