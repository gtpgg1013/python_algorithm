# https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    stack = []
    for n in number:
        while True:
            if len(stack) == 0 or k == 0:
                break
            if int(n) > int(stack[-1]):
                stack.pop()
                k -= 1
            else:
                break
        stack.append(n)

    if len(stack) != len(number)-k:
        stack = stack[:len(number)-k]

    answer = ''.join(stack)
    return answer

# 최악의 경우 N2이어서 시간초과..
# def solution(number, k):
#     origin_len = len(number)
#     for _ in range(k):
#         for i in range(len(number)-1):
#             if number[i] < number[i+1]:
#                 number = number[:i] + number[i+1:]
#                 break

#     if len(number) != origin_len - k:
#         tmp = len(number) - (origin_len-k)
#         number = number[:-tmp]

#     return number
