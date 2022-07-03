def solution(phone_number):
    length = len(phone_number)
    if length>4:
        answer = '*'*(length-4) + phone_number[length-4:length]
    else:
        answer = phone_number
    return answer