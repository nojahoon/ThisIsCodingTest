def solution(skill, skill_trees):
    answer = 0
    for user in skill_trees:
        IS_VIOLATION = False
        rule=skill
        for sk in user:
            if IS_VIOLATION == True:
                break
            if sk in rule:
                index = rule.find(sk)
                if index == 0:
                    if len(rule) > 0:
                        rule = rule[1:len(rule)]
                    else:
                        rule = ''
                    continue
                else:
                    IS_VIOLATION = True
        if IS_VIOLATION == False:
            answer += 1
    return answer