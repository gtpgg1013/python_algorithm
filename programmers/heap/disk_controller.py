# https://programmers.co.kr/learn/courses/30/lessons/42627
import heapq


def solution(jobs):
    now_time = 0
    total_time = 0
    jobs.sort(key=lambda x: (x[0], x[1]))
    len_jobs = len(jobs)

    while True:
        if len(jobs) == 0:
            break
        heap = []
        for j in jobs:
            if j[0] <= now_time:
                heapq.heappush(heap, [j[1], j[0]])
            else:
                break

        if heap:
            next_work = heapq.heappop(heap)
            now_time += next_work[0]
            total_time += (now_time - next_work[1])
            jobs.remove(next_work[::-1])
        else:
            now_time += 1

    return int(total_time / len_jobs)

# 통과 실패
# import heapq

# def solution(jobs):
#     heap = []
#     for j in jobs:
#         heapq.heappush(heap, j)

#     now_time = 0
#     total_time = 0
#     cnt = 0
#     while True:
#         if len(heap) == 0:
#             break
#         tmp_list = []
#         is_first = True

#         while True:
#             if len(heap) == 0:
#                 break
#             # if cnt == 1:
#             #     return now_time, 'lol'
#             tmp_ele = heapq.heappop(heap)
#             # if cnt == 1:
#             #     return now_time, 'lol', str(tmp_ele)
#             if is_first and tmp_ele[0] >= now_time:
#                 tmp_list.append(tmp_ele)
#                 break
#             if tmp_ele[0] <= now_time:
#                 # if cnt == 1:
#                 #     return 3
#                 tmp_list.append(tmp_ele)
#             else:
#                 heapq.heappush(heap, tmp_ele)
#                 break
#             is_first = False
#         # if cnt == 1:
#         #     return now_time, 'lol', str(tmp_list)
#         # if cnt == 1:
#         #     return 3
#         tmp_list.sort(key=lambda x:x[1])
#         # if cnt == 1:
#         #     return 3
#         add_time = now_time - tmp_list[0][0]
#         if add_time <= 0 :
#             add_time = 0
#             # return tmp_list, now_time
#         if tmp_list[0][0] > now_time :
#             add_time = tmp_list[0][1] - now_time
#             # return tmp_list, now_time
#         # if add_time <= 0 : add_time = 0
#         now_time += tmp_list[0][1]
#         total_time = total_time + (add_time) + tmp_list[0][1]

#         if len(tmp_list) > 1:
#             for t in tmp_list[1:]:
#                 heapq.heappush(heap, t)

#         # if cnt == 1:
#         #     return str(tmp_list)

#         cnt += 1

#     return int(total_time / len(jobs))
