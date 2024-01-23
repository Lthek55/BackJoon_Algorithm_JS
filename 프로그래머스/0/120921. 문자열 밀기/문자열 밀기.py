from collections import deque

def solution(A, B):
    pivot = ""
    answer = 0
    queue = deque(A)

    
    if A == B: 
        return 0
    
    for i in range(len(A)-1):
        queue.rotate(1)
        answer += 1
        result = ''.join(map(str, queue))
        
        if B == result:
            return answer
        
    return -1
    
    
    
        
        
        