def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False  
    return True

def solution(n):
    ans = []
    for i in range(2,n+1):
        if not isPrime(i): 
            continue
            
        if n % i == 0:
            ans.append(i)
            n = n // i 
        
    return ans