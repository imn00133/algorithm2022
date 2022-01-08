# chap03 그리디 - 숫자 카드 게임
# Solved Date: 21.12.30.

import sys

read = sys.stdin.readline


def solve(arr):
    row_min = [min(row) for row in arr]
    return max(row_min)


if __name__ == '__main__':
    row_num, column_num = (int(x) for x in read().split())
    arr = []
    for _ in range(row_num):
        arr.append([int(x) for x in read().split()])
    print(solve(arr))
