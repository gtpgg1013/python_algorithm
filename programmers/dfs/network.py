# https://programmers.co.kr/learn/courses/30/lessons/43162

checklist = [1] * 200
network = []


def solution(n, computers):
    global checklist
    global network
    checklist = checklist[:n]
    for idx, c in enumerate(checklist):
        if c == 1:
            tmp_set = set()
            dfs(idx, computers, tmp_set)
            network.append(tmp_set)

    answer = len(network)
    return answer


def dfs(idx, computers, tmp_set):
    checklist[idx] = 0
    tmp_set.add(idx)
    for idx_c, c in enumerate(computers[idx]):
        if idx_c == idx:
            continue
        if c == 1 and idx_c not in tmp_set:
            dfs(idx_c, computers, tmp_set)
