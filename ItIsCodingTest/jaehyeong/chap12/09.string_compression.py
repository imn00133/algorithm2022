# chap12 구현 - 문자열 압축
# Solved Date: 22.01.16.
# https://programmers.co.kr/learn/courses/30/lessons/60057
import sys

read = sys.stdin.readline


def sum_compress_len(loop_count, cache):
    if loop_count <= 1:
        return len(cache)
    return len(str(loop_count)) + len(cache)


# https://programmers.co.kr/questions/25102 참고
# 2자리인 경우 고려하지 않았음...
# index 맞춰서 돌리기
def count_compress_string(s, char_count):
    compress_len = 0
    loop_count = 0
    cache = ""
    prev_index = 0
    for index in range(0, len(s) + 1, char_count):
        if index == 0:
            continue

        sub_string = s[prev_index:index]
        prev_index = index

        if cache == sub_string:
            loop_count += 1
            continue

        compress_len += sum_compress_len(loop_count, cache)
        loop_count = 1
        cache = sub_string

    # 맨 마지막 덧셈 수행
    compress_len += sum_compress_len(loop_count, cache)
    compress_len += len(s) % char_count
    return compress_len


def solution(s):
    answer = len(s)
    max_check_len = (len(s) // 2) + 1
    for char_count in range(1, max_check_len):
        answer = min(answer, count_compress_string(s, char_count))
    return answer


# O(n^2) => 100만임으로 문제 없음
if __name__ == '__main__':
    s = read().rstrip()
    print(solution(s))
