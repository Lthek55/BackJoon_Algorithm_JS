from functools import reduce

def solution(my_string, n):
    return ''.join(map((lambda x: x*n), my_string))
