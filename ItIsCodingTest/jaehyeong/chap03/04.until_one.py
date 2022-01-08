# chap03 그리디 - 숫자 카드 게임
# Solved Date: 21.12.30.

import sys

read = sys.stdin.readline


def solve(n, k):
    ans = 0
    while n != 1:
        if n % k == 0:
            n = n // k
        else:
            n = n - 1
        ans += 1
    return ans


if __name__ == '__main__':
    n, k = (int(x) for x in read().split())
    print(solve(n, k))
