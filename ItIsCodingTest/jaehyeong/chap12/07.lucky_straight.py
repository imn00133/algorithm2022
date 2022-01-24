# chap07 구현 - 럭키 스트레이트
# Solved Date: 22.01.15.
# https://www.acmicpc.net/problem/18406
import sys

read = sys.stdin.readline


# 현재 채점 방식으로는 속도가 같음
# https://www.acmicpc.net/source/25881239 참고
def fast_solve(score):
    left_sum, right_sum = 0, 0
    half_len = len(score) // 2

    for index in range(half_len):
        left_sum += score[index]

    for index in range(half_len, len(score)):
        right_sum += score[index]

    if left_sum == right_sum:
        return "LUCKY"
    return "READY"


def solve(score):
    half_len = len(score) // 2
    if sum(score[:half_len]) == sum(score[half_len:]):
        return "LUCKY"
    return "READY"


if __name__ == '__main__':
    score = [int(x) for x in read().rstrip()]
    print(fast_solve(score))
