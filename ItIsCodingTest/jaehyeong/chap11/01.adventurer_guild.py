# chap11 그리디 - 모험가 길드
# Solved Date: 21.12.31.

import sys

read = sys.stdin.readline


# 공포도를 index로 모험가가 몇 명인지 센 리스트를 반환한다.
# counter로도 가능하나, 공포도가 낮은 사람을 먼저 확인하기 쉬운 방법은 list로 보임
def sort_adventurer(adventurer_num, adventurer_arr):
    fear_counts = [0 for x in range(adventurer_num + 1)]
    for fear in adventurer_arr:
        fear_counts[fear] += 1
    return fear_counts


# 간단하게 보면, 공포도가 낮은 사람을 우선적으로 배치하는게 중요하다. => 그룹수가 많아짐
# 공포도가 낮은 사람을 먼저 묶어 그룹을 만들 수 있는지 본다.
# 만들 수 없으면 그 다음 공포도를 가진 사람들을 포함했을 때, 그룹을 만들 수 있는지 본다.
# 이렇게 그리디하게 묶으면 가장 많은 그룹을 만들 수 있다.
def solve(fear_counts):
    remaining_adventurer = 0
    group = 0
    for fear, adventurer_count in enumerate(fear_counts):
        if fear == 0:
            continue
        remaining_adventurer += adventurer_count
        while remaining_adventurer >= fear:
            group += 1
            remaining_adventurer -= fear
    return group


if __name__ == '__main__':
    adventurer_num = int(read())
    adventurer_arr = [int(x) for x in read().split()]
    fear_counts = sort_adventurer(adventurer_num, adventurer_arr)
    print(solve(fear_counts))
