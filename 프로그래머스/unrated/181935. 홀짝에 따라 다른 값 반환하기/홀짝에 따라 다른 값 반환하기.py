def solution(n):
    start_position = 2 if n % 2 == 0 else 1
    answer = 0
    
    for i in range(start_position, n+1, 2):
        
        answer += i*i if start_position == 2 else i
    return answer