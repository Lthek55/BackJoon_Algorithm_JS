def solution(n, control):
    position = {'w':1, 's':-1, 'd':10, 'a':-10}
    answer = n
    
    for i in control:
        answer += position[i]

        
    return answer
