# chap12 구현 - 치킨배달
# Solved Date: 22.01.20.
# https://www.acmicpc.net/problem/15686
import sys
from itertools import combinations

read = sys.stdin.readline
MAX = 100000000


# kind별 위치 구하기
def find_pos(arr, kind):
    positions = []
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if arr[y][x] == kind:
                positions.append((x, y))
    return positions


# house - chicken 개수 확인
# 행으로 house를 두면 계산하기 편함
def calc_distance_arr(house_positions, chicken_positions):
    distance = [[0 for _ in range(len(chicken_positions))] for _ in range(len(house_positions))]
    for house_index, house_pos in enumerate(house_positions):
        for chicken_index, chicken_pos in enumerate(chicken_positions):
            distance[house_index][chicken_index] = abs(chicken_pos[0] - house_pos[0]) + abs(chicken_pos[1] - house_pos[1])
    return distance


# combination으로 모든 조합 확인
def calc_min_chicken_distance(chicken_num, distances):
    answer = []

    chicken_combination = combinations(range(len(distances[0])), chicken_num)
    for indexes in chicken_combination:
        sum_chicken_value = 0
        for chicken_distance in distances:
            sum_chicken_value += min([chicken_distance[i] for i in indexes])
        answer.append(sum_chicken_value)

    return min(answer)


# 집의 개수는 100개, 치킨집의 개수는 13개
# 총 distance array의 개수는 1300개
# 치킨집의 개수를 보았을 때, 최대 콤비네이션은 13C6 정도로 1716개 -> 완전 탐색 가능
def solve(chicken_num, arr):
    house_pos = find_pos(arr, '1')
    chicken_pos = find_pos(arr, '2')
    distance = calc_distance_arr(house_pos, chicken_pos)
    return calc_min_chicken_distance(chicken_num, distance)


# find_pos를 두 번 해도 크게 차이 없음
def fast_find_pos(arr):
    house_positions = []
    chicken_positions = []
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if arr[y][x] == '1':
                house_positions.append((x, y))
            elif arr[y][x] == '2':
                chicken_positions.append((x, y))
    return house_positions, chicken_positions


def calc_chicken_distance(chicken_survivals, chicken_distances):
    answer = 0
    for chicken_distance in chicken_distances:
        answer += min([chicken_distance[i] for i in chicken_survivals])
    return answer


# def로 재귀 구현
def chicken_open(available_open_num, chicken_index, chicken_survivals, min_distance, chicken_distances):
    if available_open_num == 0:
        return calc_chicken_distance(chicken_survivals, chicken_distances)

    if available_open_num > len(chicken_distances[0]) - chicken_index:
        return MAX

    if chicken_index >= len(chicken_distances[0]):
        return MAX

    chicken_survivals.append(chicken_index)
    selected_distance = chicken_open(available_open_num-1, chicken_index+1, chicken_survivals, min_distance, chicken_distances)
    chicken_survivals.pop()
    unselected_distance = chicken_open(available_open_num, chicken_index+1, chicken_survivals, min_distance, chicken_distances)
    return min(min_distance, selected_distance, unselected_distance)


# for로 재귀 구현
def chicken_open_for(available_open_num, start_index, chicken_survivals, min_distance, chicken_distances):
    if available_open_num == 0:
        return calc_chicken_distance(chicken_survivals, chicken_distances)

    for chicken_index in range(start_index, len(chicken_distances[0])):
        chicken_survivals.append(chicken_index)
        selected_distance = chicken_open(available_open_num-1, chicken_index+1, chicken_survivals, min_distance, chicken_distances)
        chicken_survivals.pop()
        if selected_distance < min_distance:
            min_distance = selected_distance

    return min_distance


# 최백준 알고리즘 기초/510 - 브루트 포스 참고
# https://www.acmicpc.net/source/36637416 참고
def fast_solve(chicken_num, arr):
    house_positions, chicken_positions = fast_find_pos(arr)
    chicken_distances = calc_distance_arr(house_positions, chicken_positions)
    return chicken_open(chicken_num, 0, [], MAX, chicken_distances)


if __name__ == "__main__":
    arr_num, chicken_num = (int(x) for x in read().split())
    arr = [read().split() for _ in range(arr_num)]
    print(solve(chicken_num, arr))
