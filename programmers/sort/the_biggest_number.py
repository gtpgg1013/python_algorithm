# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    numbers = map(str, numbers)
    sorted_numbers = sorted(numbers, key=lambda x: str(x) * 3, reverse=True)
    answer = ''
    for n in sorted_numbers:
        answer += n

    return str(int(answer))
