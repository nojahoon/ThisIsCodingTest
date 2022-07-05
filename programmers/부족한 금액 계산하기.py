def solution(price, money, count):
    sum = 0
    for i in range(1, count + 1, 1):
        sum += price * i

    if money < sum:  # 부족한 금액만큼 return
        return sum - money

    # 금액이 부족하지 않으면 0 리턴
    return 0
