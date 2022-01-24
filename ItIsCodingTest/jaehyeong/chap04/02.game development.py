# chap04 구현 - 게임개발
# Solved Date: 22.01.12.

import sys
# https://jlog1016.tistory.com/23 재귀 해제 - 하지만 문제가..
sys.setrecursionlimit(5000)
read = sys.stdin.readline

DIRECTION = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def make_check_direction(island_map):
    row_length = len(island_map)
    column_length = len(island_map[0])

    def check_direction(x, y):
        if (0 <= x < column_length) and (0 <= y < row_length):
            return True
        return False

    return check_direction


# dfs 사용 - 불가
# 약 2500개가 최대(?)여서, stack overflow가 날 가능성이 없어 사용
def dfs(island_map, character_status, character_map, check_direction):
    x, y, see_direction = character_status
    answer = 0
    is_moved = False
    for direction_index in range(len(DIRECTION)):
        move_direction = (direction_index + see_direction) % len(DIRECTION)
        dx, dy = DIRECTION[move_direction][0], DIRECTION[move_direction][1]
        check_x, check_y = x + dx, y + dy
        if check_direction(check_x, check_y) and island_map[check_y][check_x] == '0' \
            and not character_map[check_y][check_x]:
            character_map[check_y][check_x] = True
            answer += 1
            is_moved = True
            answer += dfs(island_map, (check_x, check_y, move_direction), character_map, check_direction)
    if not is_moved:
        dx, dy = -DIRECTION[see_direction][0], -DIRECTION[see_direction][1]
        x, y = x + dx, y + dy
        if check_direction(x, y) and island_map[y][x] == '0':
            answer += dfs(island_map, (x, y, see_direction), character_map, check_direction)
    return answer


# 문제풀이가 잘못됨
# 0 0 0
# 0 1 1 이고, (0, 1)에서 시작하면 완전탐색이 아님
def dfs_solve(island_map, character_status):
    check_direction = make_check_direction(island_map)
    character_map = [[False for _ in range(m)] for _ in range(n)]
    answer = dfs(island_map, character_status, character_map, check_direction)
    return answer


def while_solve(island_map, character_status):
    check_direction = make_check_direction(island_map)
    character_map = [[False for _ in range(m)] for _ in range(n)]
    x, y, see_direction = character_status

    answer = 0
    while True:
        for next_index in range(len(DIRECTION)):
            next_direction = (next_index + see_direction) % len(DIRECTION)
            dx, dy = DIRECTION[next_direction][0], DIRECTION[next_direction][1]
            nx, ny = x + dx, y + dy
            if check_direction(nx, ny) and island_map[ny][nx] == '0' and not character_map[ny][nx]:
                answer += 1
                character_map[ny][nx] = True
                x, y, see_direction = nx, ny, next_direction
                break
        else:
            dx, dy = -DIRECTION[see_direction][0], -DIRECTION[see_direction][1]
            x, y = x + dx, y + dy
            if not(check_direction(x, y) and island_map[y][x] == '0'):
                break
    return answer


# 시작 초기화 안했네;
if __name__ == '__main__':
    n, m = (int(x) for x in read().split())
    character = [int(x) for x in read().split()]
    arr = [[x for x in read().split()] for _ in range(n)]
    print(dfs_solve(arr, character))
    character_map = [[False for _ in range(m)] for _ in range(n)]
    print(while_solve(arr, character))
    # print(50, 50)
    # print(0, 0, 0)
    # for _ in range(50):
    #     print(*[0 for _ in range(50)])