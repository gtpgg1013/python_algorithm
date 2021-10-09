# global이 기억이 안나서 일단 푼 방식..

# def solution(numbers, target):
#     tmp = []
#     dfs(0, 0, numbers, target, tmp)
#     answer = len(tmp)
#     print(answer)
#     return answer


# def dfs(idx, value, numbers, target, tmp):
#     if idx == len(numbers):
#         print(idx, value)
#         if value == target:
#             tmp.append(1)
#     else:
#         minus_value = value
#         plus_value = value
#         minus_value -= numbers[idx]
#         dfs(idx+1, minus_value, numbers, target, tmp)
#         plus_value += numbers[idx]
#         dfs(idx+1, plus_value, numbers, target, tmp)

answer = 0


def solution(numbers, target):
    global answer
    dfs(0, 0, numbers, target)
    print(answer)
    return answer


def dfs(idx, value, numbers, target):
    global answer
    if idx == len(numbers):
        if value == target:
            answer += 1
        else:
            pass
    else:
        minus_value = value
        plus_value = value
        minus_value -= numbers[idx]
        dfs(idx+1, minus_value, numbers, target)
        plus_value += numbers[idx]
        dfs(idx+1, plus_value, numbers, target)


numbers = [1, 1, 1, 1, 1]
target = 3

solution(numbers, target)
