def solution(myString, pat):
    l = len(pat)
    n = len(myString) - l
    
    cnt = 0
    
    for i in range(n+1):
        pivot = myString[i:i+l]
        if pivot == pat:
            cnt +=1
    return cnt
