def solution(lottos, win_nums):
    rank = {'6': 1, '5': 2, '4': 3, '3': 4, '2': 5, '1': 6, '0': 6}
    answer = []  # 최고 순위와 최저 순위 반환
    count = 0

    for i in lottos:
        if i in win_nums:
            count += 1

    answer.append(rank[str(count + lottos.count(0))])
    answer.append(rank[str(count)])

    return answer