# chap12 구현 - 뱀
# Solved Date: 22.01.16.
# https://www.acmicpc.net/problem/3190
import sys
from collections import deque

DIRECTION = ((1, 0), (0, 1), (-1, 0), (0, -1))

read = sys.stdin.readline


# 각각 계산이 아니라, index를 1, 3을 사용해서 줄일 수 있음
# https://www.acmicpc.net/source/10893680
# 또한 -1에 대한 %4 연산은 3이 나옴
# https://www.acmicpc.net/source/15729371
def calc_direction(snake_direction, character):
    if character == 'L':
        snake_direction -= 1

    if character == 'D':
        snake_direction += 1

    return snake_direction % 4


def check_board_margin(board, x, y):
    return (0 <= x < len(board[0])) and (0 <= y < len(board))


def make_change_direction():
    position_num = int(read().rstrip())

    def change_direction():
        nonlocal position_num
        if position_num == 0:
            return -1, -1
        position_num -= 1
        position = read().split()
        return int(position[0]), position[1]

    return change_direction


def coroutine_direction():
    position_num = int(read().rstrip())
    positions = []
    for _ in range(position_num):
        second, direction = read().split()
        positions.append((int(second), direction))

    yield from positions
    yield -1, -1


# 메모리를 더 사용함
# 뱀 2
def coroutine_simulate(board):
    time = 0
    snake = deque([(0, 0)])
    board[0][0] = 2
    snake_direction = 0

    coroutine = coroutine_direction()
    change_position_time, change_position = next(coroutine)

    while True:
        time += 1
        head = snake[-1]
        direction = DIRECTION[snake_direction]
        next_x, next_y = head[0] + direction[0], head[1] + direction[1]

        if not check_board_margin(board, next_x, next_y):
            break

        board_value = board[next_y][next_x]
        if board_value == 0:
            tail = snake.popleft()
            board[tail[1]][tail[0]] = 0
        elif board_value == 2:
            break

        board[next_y][next_x] = 2
        snake.append((next_x, next_y))
        if time == change_position_time:
            snake_direction = calc_direction(snake_direction, change_position)
            change_position_time, change_position = next(coroutine)
    return time


# snake는 오른쪽이 머리로 계산
# 뱀 2
def simulate(board):
    time = 0
    snake = deque([(0, 0)])
    board[0][0] = 2
    snake_direction = 0
    direction = DIRECTION[snake_direction]

    change_direction = make_change_direction()
    change_position_time, change_position = change_direction()

    while True:
        time += 1
        head = snake[-1]
        next_x, next_y = head[0] + direction[0], head[1] + direction[1]

        if not check_board_margin(board, next_x, next_y):
            break

        board_value = board[next_y][next_x]
        if board_value == 0:
            tail = snake.popleft()
            board[tail[1]][tail[0]] = 0
        elif board_value == 2:
            break

        board[next_y][next_x] = 2
        snake.append((next_x, next_y))
        if time == change_position_time:
            snake_direction = calc_direction(snake_direction, change_position)
            change_position_time, change_position = change_direction()
            direction = DIRECTION[snake_direction]
    return time


# 참고 https://www.acmicpc.net/source/25384056
# 참고 https://www.acmicpc.net/source/19483706 -> 속도 빠르나 이제 72ms만 나옴
# 사과 -> snake length
# 사과 아님 -> collision time 증가
# 뱀의 이동 기록 = snake length + collision time
# 뱀의 이동 기록을 남기는데, collision time 보다 크면 충돌한 것으로 봄
def fast_simulate(board):
    directions = {}
    direction_num = int(read().rstrip())
    for _ in range(direction_num):
        second, direction = read().split()
        directions[int(second)] = direction

    snake = (0, 0)
    board[0][0] = 1

    snake_direction = 0
    direction = DIRECTION[snake_direction]

    snake_length = 1
    collision_time = 0

    time = 0
    while True:
        time += 1
        snake = snake[0] + direction[0], snake[1] + direction[1]
        next_x, next_y = snake

        if not check_board_margin(board, next_x, next_y):
            break

        board_value = board[next_y][next_x]
        if board_value > collision_time:
            break

        if board_value == -1:
            snake_length += 1
        else:
            collision_time += 1

        board[next_y][next_x] = snake_length + collision_time
        if time in directions:
            snake_direction = calc_direction(snake_direction, directions[time])
            direction = DIRECTION[snake_direction]
    return time


# map: 0: 비어있음, -1: 사과
# import collections가 무거움 -> import collections만 삭제해도 24ms가 빨라짐(92ms -> 68ms)
if __name__ == '__main__':
    arr_num = int(read().rstrip())
    board = [[0 for _ in range(arr_num)] for _ in range(arr_num)]

    apple_num = int(read().rstrip())
    for _ in range(apple_num):
        apple_y, apple_x = (int(x) - 1 for x in read().split())
        board[apple_y][apple_x] = -1

    print(fast_simulate(board))
