# https://programmers.co.kr/learn/courses/30/lessons/43163
min_val = 10000


def solution(begin, target, words):
    global min_val
    words = set(words)
    if target not in words:
        min_val = 0

    dfs(begin, target, words, 0)

    if min_val == 10000:
        return 0
    return min_val


def transable(w1, w2):
    global min_val
    ck = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            ck += 1
    if ck == 1:
        return True
    else:
        return False


def dfs(now_word, target, now_set, cnt):
    global min_val
    now_list = list(now_set)
    for w in now_list:
        if transable(now_word, w):
            cnt += 1
            if target == w and cnt < min_val:
                min_val = cnt
                break
            now_set.discard(w)
            dfs(w, target, now_set, cnt)
            cnt -= 1
            now_set.add(w)
        else:
            continue
