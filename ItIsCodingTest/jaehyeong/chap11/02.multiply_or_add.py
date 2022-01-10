# chap11 그리디 - 곱하기 혹은 더하기
# Solved Date: 21.12.31.

import sys

read = sys.stdin.readline


# 0, 1일 때만 더하고, 나머지는 곱하는 게 제일 커짐
# 현재 값과 다음 값이 0, 1일 때만 더하면 해결됨
def solve(number_arr):
    ans = 0
    for number in number_arr:
        if ans in [0, 1]:
            ans += number
            continue
        if number in [0, 1]:
            ans += number
        else:
            ans *= number
    return ans


if __name__ == '__main__':
    # 이럴 때는 input이 편함 \n문제
    number_arr = [int(x) for x in read().rstrip()]
    print(solve(number_arr))
