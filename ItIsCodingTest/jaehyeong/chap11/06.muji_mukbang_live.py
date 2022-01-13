# chap11 그리디 - 무지의 먹방 라이브
# Solved Date: 22.01.06.
# https://programmers.co.kr/learn/courses/30/lessons/42891

import sys

read = sys.stdin.readline


def solution(food_times, k):
    food_times_index = [(food_time, index) for index, food_time in enumerate(food_times)]
    food_times_index.sort()

    prev_food_time = 0
    for index, food_time_index in enumerate(food_times_index):
        current_food_time = food_time_index[0]
        next_k = k - ((current_food_time - prev_food_time) * (len(food_times_index) - index))
        prev_food_time = current_food_time

        if next_k == 0:
            for answer_index in range(index, len(food_times_index)):
                if food_times_index[answer_index][0] > current_food_time:
                    return food_times_index[answer_index]
        if next_k < 0:
            answer_index = k & (len(food_times_index) - index) + index + 1
            return food_times_index[answer_index]
        if next_k > 0:
            k = next_k


if __name__ == '__main__':
    k = int(read().rstrip())
    food_times = [int(x) for x in read().split()]
    print(solution(food_times, k))
