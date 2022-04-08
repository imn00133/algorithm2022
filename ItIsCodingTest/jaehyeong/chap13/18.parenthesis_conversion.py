# 13 DSP/BFS문제 - 괄호 변환
# Solved Date: 22.03.25.
# https://www.acmicpc.net/problem/14502


def convert_u_is_not_right(u):
    conversion_u = []
    for letter in u[1:-1]:
        addition_p = '('
        if letter == '(':
            addition_p = ')'
        conversion_u.append(addition_p)
    return "".join(conversion_u)


def check_right_parenthesis(p):
    stack = []
    for letter in p:
        if letter == ')':
            if not stack:
                return False
            stack.pop()
        else:
            stack.append(letter)
    return not stack


def check_balance_parenthesis(p):
    left_count, right_count = 0, 0
    for index, letter in enumerate(p):
        if letter == '(':
            left_count += 1
        else:
            right_count += 1
        if left_count == right_count:
            return index
    return len(p)


def balance_parenthesis_conversion(p):
    if not p or check_right_parenthesis(p):
        return p
    # u는 더 작은 균형잡힌 괄호문자열이 될 수 없기 때문에, 가장 최소로 뽑음
    balance_index = check_balance_parenthesis(p) + 1
    u = p[:balance_index]
    v = p[balance_index:]
    if check_right_parenthesis(u):
        return u + balance_parenthesis_conversion(v)
    else:
        return "(" + balance_parenthesis_conversion(v) + ")" + convert_u_is_not_right(u)


def solution(p):
    return balance_parenthesis_conversion(p)


if __name__ == "__main__":
    parenthesis = "()))((()"
    problem_answer = "()(())()"
    print(solution(parenthesis))
    print(solution(parenthesis) == problem_answer)
