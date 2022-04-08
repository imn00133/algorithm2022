# 13 DSP/BFS문제 - 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888
# Solved Date: 20.05.12.
# 500BruteForce에서 풀었던 내용을 그대로 가져옴

import sys
import itertools

read = sys.stdin.readline
MAX = 10 ** 9
MIN = -(10 ** 9)


def next_permutation(operators):
    end_index = -1
    for index in range(len(operators)-1, 0, -1):
        if operators[index-1] < operators[index]:
            end_index = index - 1
            break
    if end_index == -1:
        return False
    swap_index = len(operators) - 1
    swap_num = 4
    for index in range(end_index+1, len(operators)):
        if swap_num >= operators[index] > operators[end_index]:
            swap_num = operators[index]
            swap_index = index
    operators[end_index], operators[swap_index] = operators[swap_index], operators[end_index]
    j = len(operators)
    while True:
        end_index += 1
        j -= 1
        if end_index >= j:
            break
        operators[end_index], operators[j] = operators[j], operators[end_index]
    return True


def permutation(nums, operation_count):
    operators = []
    for index in range(len(operation_count)):
        for _ in range(operation_count[index]):
            operators.append(index)
    max_num = MIN
    min_num = MAX
    while True:
        value = nums[0]
        for index in range(len(operators)):
            value = operation_calc(value, nums[index+1], operators[index])
        if max_num < value:
            max_num = value
        if min_num > value:
            min_num = value
        if not next_permutation(operators):
            break
    return max_num, min_num


def operation_calc(num1, num2, index):
    if index == 0:
        return num1 + num2
    elif index == 1:
        return num1 - num2
    elif index == 2:
        return num1 * num2
    else:
        if num1 < 0:
            return -(-num1 // num2)
        else:
            return num1 // num2


def recursion(nums, operation_count, sum_num, index=1):
    if index == len(nums):
        return sum_num, sum_num
    calc = []
    for operation_index in range(len(operation_count)):
        if operation_count[operation_index]:
            operation_count[operation_index] -= 1
            calc_value = operation_calc(sum_num, nums[index], operation_index)
            calc.append(recursion(nums, operation_count, calc_value, index+1))
            operation_count[operation_index] += 1
    max_nums, min_nums = zip(*calc)
    return max(max_nums), min(min_nums)


def main(mode=''):
    arr_num = int(read().strip())
    nums = [int(x) for x in read().split()]
    operation_count = [int(x) for x in read().split()]
    if mode == 'permutation':
        ans = permutation(nums, operation_count)
    else:
        ans = recursion(nums, operation_count, nums[0])
    print(*ans, sep='\n')


if __name__ == '__main__':
    main('permutation')
