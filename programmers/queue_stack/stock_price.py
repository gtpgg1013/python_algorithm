# https://programmers.co.kr/learn/courses/30/lessons/42584#

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for k in range(i+1, len(prices)):
            if prices[i] <= prices[k]:
                answer[i] += 1
            else:
                answer[i] += 1
                break

    return answer
