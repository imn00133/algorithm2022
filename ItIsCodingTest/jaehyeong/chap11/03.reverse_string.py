# chap11 그리디 - 문자열 뒤집기
# https://www.acmicpc.net/problem/1439
# Solved Date: 21.12.31.

import sys

read = sys.stdin.readline


# https://www.acmicpc.net/source/17013841 참고
def easy_index_solve(number_string):
    ans = 1
    for index in range(len(number_string)):
        if number_string[index] != number_string[index-1]:
            ans += 1
    return ans // 2


def index_solve(number_string):
    ans = 1
    prev_index = 0
    for index in range(1, len(number_string)):
        if number_string[index] != number_string[prev_index]:
            ans += 1
            prev_index = index
    return ans // 2


# https://www.acmicpc.net/source/13436438 참고
# 좀 더 간단한 풀이
def easy_solve(number_string):
    ans = 0
    prev = ''
    for number in number_string:
        if prev != number:
            prev = number
            ans += 1
    return ans // 2


# 0과 1이 바뀌는 부분을 전부 계산
# 대칭이 아닐 경우 0과 1이 바뀌는 부분이 홀수 == 양쪽 끝이 다른 상태
# 양쪽 끝이 다른 것은 +1번 추가하고 다른 부분을 땔 수 있다.
# 결국 양쪽이 같은 상태로 계산됨
# 양쪽이 같은 상태는 총 변경 횟수에 // 2를 함
# => 가까운 내부를 반전해서 양쪽끝을 맞추는 것과 같기 때문에 절반만 필요하다.
def solve(number_string):
    ans = 0
    for index, number in enumerate(number_string):
        if index == len(number_string) - 1:
            break
        if number_string[index + 1] != number:
            ans += 1
    if ans % 2 == 0:
        ans = ans // 2
    else:
        ans = ans // 2 + 1
    return ans


# 54ms 까지 속도가 났지만, 최근에는 나타나지 않음.
# 서버 속도에 따라 이 정도 차이는 날 수 있음
# 매우 짧고 간단한 것도 68ms가 나는 걸로 봐서 더 빠르게는 불가능 https://www.acmicpc.net/source/25293415
# input과 read().rstrip()의 차이는 없음
if __name__ == '__main__':
    number_string = read().rstrip()
    print(easy_index_solve(number_string))
