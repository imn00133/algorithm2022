# 06 정렬 - 두 배열의 원소 교체
# Solved Date: 22.04.08.
import sys

read = sys.stdin.readline

if __name__ == '__main__':
    arr_num, k = (int(x) for x in read().split())
    arr_a = sorted([int(x) for x in read().split()])
    arr_b = sorted([int(x) for x in read().split()])

    for index in range(arr_num):
        if index >= k:
            break

        reverse_index = arr_num - index - 1
        if arr_a[index] == arr_b[reverse_index]:
            break
        arr_a[index] = arr_b[reverse_index]

    print(sum(arr_a))
