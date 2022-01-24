# chap04 구현 - 왕실의 나이트
# Solved Date: 22.01.12.

import sys

read = sys.stdin.readline

POS = ((2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2))


def solve(position):
    answer = 0
    for dx, dy in POS:
        if (ord('a') <= ord(position[0]) + dx <= ord('h')) and (1 <= int(position[1]) + dy <= 8):
            answer += 1
    return answer


if __name__ == '__main__':
    knight_position = read().rstrip()
    print(solve(knight_position))
