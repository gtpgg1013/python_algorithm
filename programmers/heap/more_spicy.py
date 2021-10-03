# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq


def solution(scoville, K):
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)

    cnt = 0
    while True:
        a = heapq.heappop(heap)
        if a >= K:
            return cnt
        if len(heap) == 0:
            return -1
        b = heapq.heappop(heap)
        mixed = a + 2 * b
        heapq.heappush(heap, mixed)
        cnt += 1
