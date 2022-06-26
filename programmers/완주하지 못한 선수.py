def solution(participant, completion):
    dict = {}
    sum_hash = 0

    for person in participant:
        dict[hash(person)] = person
        sum_hash += hash(person)

    for person in completion:
        sum_hash -= hash(person)

    return dict[sum_hash]