# https://programmers.co.kr/learn/courses/30/lessons/42860#

def solution(name):
    a_dict = {chr(65+i): i for i in range(26)}
    name_list = list(name)
    name_list = [min(abs(26-a_dict[n]), a_dict[n]) for n in name_list]

    len_name = len(name_list)

    idx = 0
    answer = 0
    flag = 0

    while True:
        if name_list[idx] != 0:
            answer += name_list[idx]
            name_list[idx] = 0

        if sum(name_list) == 0:
            break

        idx_right = idx
        cnt_right = 0
        while True:
            if idx_right >= len_name-1:
                cnt_right = 250
                break
            idx_right += 1
            cnt_right += 1
            if name_list[idx_right] != 0:
                break

        idx_left = idx
        cnt_left = 0
        while True:
            idx_left -= 1
            cnt_left += 1
            if idx_left < 0:
                idx_left = len_name-1
            if name_list[idx_left] != 0:
                break

        if cnt_left < cnt_right:
            idx = idx_left
            answer += cnt_left
        else:
            idx = idx_right
            answer += cnt_right

    return answer
