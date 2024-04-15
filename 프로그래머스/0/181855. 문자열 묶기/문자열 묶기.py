def solution(strArr):
    pivot = [0] * len(strArr)
    
    for i in strArr:
        pivot[len(i)] +=1
        
    return max(pivot)