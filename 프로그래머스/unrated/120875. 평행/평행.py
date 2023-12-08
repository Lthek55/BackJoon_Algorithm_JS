from itertools import permutations

def solution(dots):
    pivot_arr = list(permutations(dots,4))
    for i,j,k,m in pivot_arr:
        a = i[0] - j[0]
        b = i[1] - j[1]
        c = k[0] - m[0]
        d = k[1] - m[1]
        if b/a == d/c:
            return 1
    return 0
