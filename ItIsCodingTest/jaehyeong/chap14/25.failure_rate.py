# 14 정렬 - 실패율
# Solved Date: 22.04.08.
# https://programmers.co.kr/learn/courses/30/lessons/42889


def solution(N, stages):
    fail_rate = [[index+1, 0] for index in range(N)]

    # 전체 인원은 stages로 계산 가능
    # 모든 풀이에 보이는 건 o(n^2)이라 이게 더 빠르지 않을까(?)
    part_sum = 0
    for stage in stages:
        if stage == N+1:
            part_sum += 1
            continue
        fail_rate[stage-1][1] += 1

    for index in range(N):
        index += 1
        part_sum += fail_rate[-index][1]
        if part_sum == 0:
            fail_rate[-index][1] = 0.0
            continue
        fail_rate[-index][1] /= part_sum

    # 정렬 안정성이 보장됨
    fail_rate.sort(key=lambda x: -x[1])
    answer, _ = tuple(zip(*fail_rate))

    return list(answer)


if __name__ == '__main__':
    print(solution(4, [2, 2, 2]))
