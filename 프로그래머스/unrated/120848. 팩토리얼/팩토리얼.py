def fact(n):
    if n==0 or n==1:
        return 1
    return fact(n-1)*n

def solution(n):
    cnt = 11
    while True:
        pivot = fact(cnt)
        if pivot <=n:
            return cnt
        cnt-=1
        