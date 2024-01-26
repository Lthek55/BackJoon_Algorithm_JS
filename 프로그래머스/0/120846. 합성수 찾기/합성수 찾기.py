def solution(n):
    pivot = 0
    ans = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            if i % j ==0:
                pivot += 1
        if pivot >= 3: 
            ans += 1
        pivot = 0
        
    return ans
        