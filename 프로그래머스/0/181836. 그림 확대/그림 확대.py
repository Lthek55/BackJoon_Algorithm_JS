def solution(picture, k):
    answer = []
    
    for i in picture: 
        pivot = []
        for j in list(i):
            pivot.append(j*k)
        
        for n in range(k):
            answer.append(''.join(pivot))
    
    return answer