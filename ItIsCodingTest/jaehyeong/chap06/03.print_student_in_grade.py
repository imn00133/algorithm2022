# 06 정렬 - 성적이 낮은 순서로 학생 출력하기
# Solved Date: 22.04.08.
import sys

read = sys.stdin.readline

if __name__ == '__main__':
    input_num = int(read().rstrip())
    arr = list()
    for _ in range(input_num):
        student, score = read().split()
        arr.append((student, score))
    arr.sort(key=lambda score: score[1])
    student_name, _ = zip(*arr)
    print(*student_name, sep=' ')
