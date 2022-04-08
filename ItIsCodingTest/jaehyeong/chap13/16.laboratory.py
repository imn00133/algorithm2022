# 13 DSP/BFS문제 - 연구소
# Solved Date: 22.03.25.
# https://www.acmicpc.net/problem/14502

from collections import deque
import sys
from itertools import combinations

read = sys.stdin.readline


DXY = ((1, 0), (0, 1), (-1, 0), (0, -1))


def solution(array, virus_pos, new_wall_positions):
    check = [[False for _ in range(len(array[0]))] for _ in range(len(array))]
    for x, y in new_wall_positions:
        check[y][x] = True

    queue = deque()
    virus_num = 0
    for x, y in virus_pos:
        check[y][x] = True
        queue.append((x, y))
        virus_num += 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in DXY:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= len(array[0]) or ny < 0 or ny >= len(array):
                continue
            if check[ny][nx] or array[ny][nx] == '1':
                continue
            check[ny][nx] = True
            virus_num += 1
            queue.append((nx, ny))
    return virus_num


def check_array(array):
    empty_positions = []
    virus_positions = []
    for y in range(len(array)):
        for x in range(len(array[0])):
            value = array[y][x]
            if value == '0':
                empty_positions.append((x, y))
            elif value == '2':
                virus_positions.append((x, y))
    return empty_positions, virus_positions


def main(array):
    empty_pos, virus_pos = check_array(array)
    making_wall_pos = combinations(empty_pos, 3)
    virus_num = len(array) * len(array[0])
    for new_wall_positions in making_wall_pos:
        virus_num = min(virus_num, solution(array, virus_pos, new_wall_positions))
    return len(empty_pos) + len(virus_pos) - virus_num - 3


if __name__ == "__main__":
    row, column = (int(x) for x in read().split())
    array = []
    for _ in range(row):
        array.append(read().split())
    print(main(array))
