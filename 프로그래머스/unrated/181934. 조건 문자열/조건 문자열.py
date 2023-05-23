

def solution(ineq, eq, n, m):
    return int(eval(f"{n}{ineq}{eq}{m}") if eq != '!' else eval(f"{n}{ineq}{m}"))