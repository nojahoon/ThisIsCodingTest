def solution(citations):

    max_citation = max(citations)

    while (max_citation >= 0):
        count = 0
        for citation in citations:
            if max_citation <= citation:
                count += 1
        if count >= max_citation:
            break
        max_citation -= 1

    if max_citation == -1:
        max_citation = 0

    answer = max_citation
    return answer