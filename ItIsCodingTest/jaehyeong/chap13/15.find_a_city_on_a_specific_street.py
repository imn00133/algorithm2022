# 13 DSP/BFS문제 - 특정 거리의 도시 찾기
# Solved Date: 22.03.17.
# https://www.acmicpc.net/problem/18352
import sys
from collections import deque

read = sys.stdin.readline


def solution(array, check_road_num, start_city):
    check_array = [False for _ in range(len(array))]
    check_array[start_city] = True

    queue = deque()
    answer = []
    queue.append((start_city, 0))
    while queue:
        current_pos, moved_road = queue.popleft()
        if moved_road == check_road_num:
            answer.append(current_pos)
        elif moved_road > check_road_num:
            break
        for next_pos in array[current_pos]:
            if check_array[next_pos]:
                continue
            check_array[next_pos] = True
            queue.append((next_pos, moved_road + 1))
    if not answer:
        answer.append(-1)
    # 들어오는 값의 순서가 꼭 맞지 않음
    return sorted(answer)


if __name__ == '__main__':
    city_num, road_num, check_road_num, start_city = (int(x) for x in read().split())
    array = [[] for _ in range(city_num + 1)]
    for _ in range(road_num):
        start, end = (int(x) for x in read().split())
        array[start].append(end)
    print(*solution(array, check_road_num, start_city), sep='\n')
