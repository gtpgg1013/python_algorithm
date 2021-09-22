# https://programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque(progresses)
    queue_speeds = deque(speeds)
    while len(queue) > 0:
        cnt = 0
        for i in range(len(queue)):
            queue[i] += queue_speeds[i]
        cnt = checknextleft(queue, queue_speeds, cnt)
        if cnt != 0:
            answer.append(cnt)
    return answer

def checknextleft(queue, queue_speeds, cnt):
    if len(queue) == 0:
        return cnt
    pop = queue.popleft()
    ps = queue_speeds.popleft()
    
    if pop >= 100:
        cnt += 1
        return checknextleft(queue, queue_speeds, cnt)
        
    else:
        queue.appendleft(pop)
        queue_speeds.appendleft(ps)
        return cnt