# 13 DSP/BFS문제 - 감시 피하기
# Solved Date: 22.04.01.
# https://www.acmicpc.net/problem/18428
import sys
from itertools import combinations
from collections import deque

read = sys.stdin.readline
DXY = ((1, 0), (0, 1), (-1, 0), (0, -1))


# object_pos대신 array에 = O를 저장하게 하였으나 속도는 같음
def did_student_run_away(array, teacher_pos, obj):
    object_pos = [[False for _ in range(len(array[0]))] for _ in range(len(array))]
    for obj_x, obj_y in obj:
        object_pos[obj_y][obj_x] = True

    queue = deque()
    for teacher_x, teacher_y in teacher_pos:
        for direction in range(len(DXY)):
            queue.append((teacher_x, teacher_y, direction))

    while queue:
        x, y, direction = queue.popleft()
        dx, dy = DXY[direction]
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= len(array[0]) or ny < 0 or ny >= len(array):
            continue

        if object_pos[ny][nx]:
            continue

        if array[ny][nx] == 'S':
            return False

        queue.append((nx, ny, direction))
    return True


# https://www.acmicpc.net/submit/18428 참고해보고 stack으로 변경 => 96ms
def stack_did_student_run_away(array, teacher_pos, obj):
    for obj_x, obj_y in obj:
        array[obj_y][obj_x] = 'O'

    stack = list()
    for teacher_x, teacher_y in teacher_pos:
        for direction in range(len(DXY)):
            stack.append((teacher_x, teacher_y, direction))

    while stack:
        x, y, direction = stack.pop()
        dx, dy = DXY[direction]
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= len(array[0]) or ny < 0 or ny >= len(array):
            continue

        if array[ny][nx] == 'O':
            continue

        if array[ny][nx] == 'S':
            for obj_x, obj_y in obj:
                array[obj_y][obj_x] = 'X'
            return False

        stack.append((nx, ny, direction))
    return True


def find_teacher_and_student(array):
    teacher_pos = []
    empty_pos = []
    for y in range(len(array)):
        for x in range(len(array[0])):
            if array[y][x] == 'T':
                teacher_pos.append((x, y))
            elif array[y][x] == 'X':
                empty_pos.append((x, y))
    return teacher_pos, empty_pos


def main():
    array_num = int(read().strip())
    array = []
    for _ in range(array_num):
        array.append(read().split())
    teacher_pos, empty_pos = find_teacher_and_student(array)
    objects = combinations(empty_pos, 3)
    for obj in objects:
        if stack_did_student_run_away(array, teacher_pos, obj):
            return "YES"
    return "NO"


if __name__ == '__main__':
    print(main())
