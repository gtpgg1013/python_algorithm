# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    feasible_yellow_set = []
    for i in range(yellow):
        if yellow % (i+1) == 0:
            feasible_yellow_set.append([int(yellow/(i+1)), (i+1)])
        if i > yellow / 2 + 1:
            break

    feasible_whole_set = []
    for k in range(brown+yellow):
        if (brown+yellow) % (k+1) == 0:
            feasible_whole_set.append([int((brown+yellow)/(k+1)), (k+1)])
        if k > (brown+yellow) / 2 + 1:
            break

    for fw in feasible_whole_set:
        for fy in feasible_yellow_set:
            if fw[0] >= fy[0] + 2 and fw[1] >= fy[1] + 2:
                return fw
