def solution(a, d, included):
    answer = 0
    
    for v in included:
        if v :
            # print(v,a, answer)
            answer = answer + a
            
        a = a+d
        
    return answer