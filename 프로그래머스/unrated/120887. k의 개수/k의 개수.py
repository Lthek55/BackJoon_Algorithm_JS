def solution(i, j, k):
    pivot = list(range(i,j+1))
    cnt = 0
    for i in pivot:
        if str(k) in str(i):
            cnt+=str(i).count(str(k))
            
    return cnt