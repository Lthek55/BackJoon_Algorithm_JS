def solution(n):
    answer = 1
    cnt = 1
    while True:
        if '3' in str(answer) or answer %3==0:
            answer +=1
        else:
            cnt+=1
            if cnt > n:
                break
            answer +=1
            
        
    return answer
