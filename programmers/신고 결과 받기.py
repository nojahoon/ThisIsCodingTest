def solution(id_list, report, k):
    answer = []
    bad_user = dict()
    email = dict()

    for id in id_list:
        bad_user[id] = 0
        email[id] = []
    for rep in report:
        record = rep.split(' ')
        reporting = record[0]
        reported = record[1]
        if reported not in email[reporting]:
            bad_user[reported] += 1
            email[reporting].append(reported)
    for id in id_list:
        count = 0
        for judge_pause in email[id]:
            if int(bad_user[judge_pause]) >= k:
                count += 1
        answer.append(count)
    return answer