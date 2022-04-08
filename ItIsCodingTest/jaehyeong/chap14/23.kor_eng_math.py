# 14 정렬 - 국영수
# Solved Date: 22.04.08.
# https://www.acmicpc.net/problem/10825
import sys

read = sys.stdin.readline


def print_for(arr):
    arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
    for score in arr:
        print(score[0])


# 380ms -> 556ms
def print_zip(arr):
    arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
    name, _, _, _ = zip(*arr)
    print(*name, sep='\n')


# 참고 https://www.acmicpc.net/source/37179899
# 380ms
def print_once(arr):
    print(*map(lambda x: x[0], sorted(arr, key=lambda x: (-x[1], x[2], -x[3], x[0]))), sep='\n')


# sort: 380ms, sorted로 받아옴: 408ms
# arr_copy = sorted(arr, key=lambda x: (-x[1], x[2], -x[3], x[0]))
# 정렬 안정성이 보장
# https://docs.python.org/ko/3/howto/sorting.html#sort-stability-and-complex-sorts
if __name__ == '__main__':
    arr_num = int(read().rstrip())
    arr = list()
    for _ in range(arr_num):
        name, kor, eng, math = read().split()
        arr.append((name, int(kor), int(eng), int(math)))

    print_once(arr)
