# 06 정렬 - 위에서 아래로
# Solved Date: 22.04.08.
import sys

read = sys.stdin.readline

if __name__ == '__main__':
    input_num = int(read().rstrip())
    arr = list()
    for _ in range(input_num):
        arr.append(int(read().rstrip()))
    arr.sort(reverse=True)
    print(*arr, sep=' ')
