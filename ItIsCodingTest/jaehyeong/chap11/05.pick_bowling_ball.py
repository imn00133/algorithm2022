# chap11 그리디 - 볼링공 고르기
# Solved Date: 22.01.06.

import sys

read = sys.stdin.readline


# 새로운 볼링공 무게와 같은 무게의 개수가 아닌 볼링공들은 전부 짝이 됨
# 따라서, 이번 인덱스에서 이전에 같은 무게의 볼링공을 빼주면 이번 인덱스의 볼링공 조합이 됨
def solve(max_weight, arr):
    combination = 0
    weight_count = [0 for _ in range(max_weight + 1)]
    for index, bowling_weight in enumerate(arr):
        combination += index - weight_count[bowling_weight]
        weight_count[bowling_weight] += 1
    return combination


if __name__ == '__main__':
    bowling_num, max_weight = (int(x) for x in read().split())
    arr = [int(x) for x in read().split()]
    print(solve(max_weight, arr))
