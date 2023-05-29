def solution(n):
    return sum(filter(lambda x: x%2==0, list(range(n+1))))