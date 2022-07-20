def solution(nums):
    dict = {}
    pick = len(nums) // 2

    for num in nums:
        dict[hash(num)] = 0

    length = len(dict.keys())

    for i in range(pick, -1, -1):
        if i <= length:
            return i