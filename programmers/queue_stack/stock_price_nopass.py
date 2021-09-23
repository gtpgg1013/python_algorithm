# https://programmers.co.kr/learn/courses/30/lessons/42584#

from collections import deque


def solution(prices):
    answer = deque([])
    queue = deque(prices)
    min_num = 10001
    min_idx = -1

    len_queue = len(queue)
    for i in range(len_queue):
        cnt = 0
        if i == 0:
            cb = 0
        else:
            cb = checknext(len_queue-1-i, len_queue-1-i, cnt, queue)

        answer.appendleft(cb)

    answer = list(answer)
    return answer


def checknext(org_idx, idx, cnt, queue):
    if idx >= 0 and idx < len(queue)-1:
        if queue[org_idx] <= queue[idx+1]:
            cnt += 1
            return checknext(org_idx, idx+1, cnt, queue)
        else:
            cnt += 1
            return cnt
    else:
        return cnt
