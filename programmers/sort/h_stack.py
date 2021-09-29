# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    sorted_citations = sorted(citations)
    answer = 0
    for idx, c in enumerate(sorted_citations):
        if c >= len(sorted_citations) - idx:
            return len(sorted_citations) - idx
    return answer
