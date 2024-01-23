def solution(t, p):
    tLen = len(t)
    pLen = len(p)
    answer = 0    
    
    for i in range(0, tLen):
        window = t[i:i+pLen]
        
        if len(window) < pLen:
            break
            
        if int(window) <= int(p):
            answer +=1
            
    return answer