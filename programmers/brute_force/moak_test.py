# https://programmers.co.kr/learn/courses/30/lessons/42840#

def solution(answers):
    num_1 = [1, 2, 3, 4, 5]
    num_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    a_len = len(answers)
    if a_len == 0:
        return [1, 2, 3]

    if len(num_1) <= a_len:
        num_1 = num_1 * ((a_len) // len(num_1) + 1)
    if len(num_2) <= a_len:
        num_2 = num_2 * ((a_len) // len(num_2) + 1)
    if len(num_3) <= a_len:
        num_3 = num_3 * ((a_len) // len(num_3) + 1)

    cnt_list = [0, 0, 0]
    for i in range(a_len):
        if num_1[i] == answers[i]:
            cnt_list[0] += 1
        if num_2[i] == answers[i]:
            cnt_list[1] += 1
        if num_3[i] == answers[i]:
            cnt_list[2] += 1

    result = []
    max_ans = max(cnt_list)
    for i in range(len(cnt_list)):
        if max_ans == cnt_list[i]:
            result.append(i + 1)

    return result
