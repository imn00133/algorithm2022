# chap03 그리디 - 큰 수의 법칙
# Solved Date: 21.12.30.

import sys

read = sys.stdin.readline


def find_max_value(arr):
    maximum_num = -1
    second_maximum = -1
    for number in arr:
        if maximum_num <= number:
            second_maximum = maximum_num
            maximum_num = number
    return [maximum_num, second_maximum]


# 좀 더 간단하게는 전체 횟수를 구하고, 이 중 maximum[0]만 구하서 더함, maximum[1]은 나머지로 더한다.
def solve(whole_addition_count, continuous_index, maximums):
    index_count = whole_addition_count // (continuous_index + 1)
    remainder = whole_addition_count % (continuous_index + 1)
    answer = 0
    answer += (maximums[0] * continuous_index + maximums[1]) * index_count
    answer += maximums[0] * remainder
    return answer


if __name__ == '__main__':
    arr_num, whole_addition_count, continuous_index = (int(x) for x in read().split())
    arr = [int(x) for x in read().split()]
    maximums = find_max_value(arr)
    print(solve(whole_addition_count, continuous_index, maximums))
