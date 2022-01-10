# chap11 그리디 - 만들 수 없는 금액
# Solved Date: 21.12.31.
import collections
import sys

read = sys.stdin.readline


# 원하는 값을 index로 치환해서 그 때까지의 값을 다 더했을 때, 원하는 값이 나오지 않으면 만들 수 없는 금액
# 원하는 값을 x라 했을 때, 통과했을 때 x-1 까지는 조합이 있음을 뜻함.
# 1 - 1이 무조건 필요
# 2 - 1, 1이거나 1, 2
# 3 - 1, 1, 1이거나 1, 2거나 3 => 이전 조합에 1이 더해지거나, 원 index필요
# 4 - 3의 조합에 1 추가 또는 2 추가 -> 이전 조합에 1이 더해지거나, 2가 더해지거나, 원 idnex필요
# 즉 x-1까지 조합이 전부 존재하기 때문에 x 인덱스까지 더한 값이 x보다 크다면 항상 만들 수 있음
# current x를 만들고 싶다. x 이하의 current를 다 더했을 때, 더한 값이 x보다 크다면 x를 만들 수 있다.
# 작은 순으로 정렬한 후 작은 수부터 하나씩 가져간다. 이 때 만들 수 있는 최대값 x는 x이하의 값을 전부 만들 수 있다.
# 어떠한 수가 오더라도, x-1까지 전부 만들 수 있기 때문에 최대값만 계산하면 가능하다.
def solve(arr_counter):
    current = 0
    current_total = 0
    while True:
        current += 1
        current_total += arr_counter[current] * current
        if current_total < current:
            break

    return current


if __name__ == '__main__':
    arr_num = int(read().rstrip())
    arr = [int(x) for x in read().split()]
    # collections를 썼으나
    # 사용할 수 없을 경우에는 0으로 초기화된 화폐단위까지의 list를 쓰거나, dictionary로 만들 수 있음
    arr_counter = collections.Counter(arr)
    print(solve(arr_counter))
