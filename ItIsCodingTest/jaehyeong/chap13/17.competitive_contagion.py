# 13 DSP/BFS문제 - 경쟁적 전염
# Solved Date: 22.03.24.
# https://www.acmicpc.net/problem/18405
import sys
from collections import deque

read = sys.stdin.readline

DXY = ((1, 0), (0, 1), (-1, 0), (0, -1))


def solution(array, virus_positions, check_second, answer_x, answer_y):
    queue = deque()
    for virus, pos_list in enumerate(virus_positions):
        if not pos_list:
            continue
        for pos in pos_list:
            queue.append((pos[0], pos[1], 0))
    while queue:
        x, y, second = queue.popleft()
        if second >= check_second:
            break
        for dx, dy in DXY:
            nx, ny = x + dx, y + dy
            if 0 > nx or len(array[0]) <= nx or 0 > ny or len(array) <= ny:
                continue
            if array[ny][nx]:
                continue
            array[ny][nx] = array[y][x]
            queue.append((nx, ny, second+1))
    return array[answer_x][answer_y]


# 스터디에서 알려준 방법
def fast_solution(array, virus_positions, check_second, answer_x, answer_y):
    answer_virus = 0
    min_dist = len(array) * 2 + 1
    for virus, pos_list in enumerate(virus_positions):
        pass
    return answer_virus


if __name__ == '__main__':
    array_num, virus_num = (int(x) for x in read().split())
    array = []
    virus_positions = [[] for _ in range(virus_num+1)]
    for y in range(array_num):
        row = [int(tube) for tube in read().split()]
        for x, virus in enumerate(row):
            if not virus:
                continue
            virus_positions[virus].append((x, y))
        array.append(row)
    check_second, answer_x, answer_y = (int(x) for x in read().split())
    print(solution(array, virus_positions, check_second, answer_x-1, answer_y-1))
