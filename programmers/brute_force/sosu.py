# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations


def solution(numbers):
    cnt = 0
    numbers = list(numbers)

    num_set = set()
    for i in range(len(numbers)):
        for num in set(list(permutations(numbers, i+1))):
            num = int(''.join(num))
            if num < 2:
                continue
            is_sosu = True
            for k in range(2, num):
                if num % (k) == 0:
                    is_sosu = False
                    break
            if is_sosu:
                num_set.add(num)
        cnt += len(num_set)

    return len(num_set)
