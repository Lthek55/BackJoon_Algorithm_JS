def solution(hp):
    attack_point = [5,3,1]
    start = 0
    answer = 0
    
    while hp != 0:
        answer += hp // attack_point[start]
        hp %= attack_point[start]
        
        if hp < attack_point[start]:
            start += 1
            
    return answer
            
