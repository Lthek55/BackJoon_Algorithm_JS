def solution(numLog):
    answer = ''
    
    num_position = {'1':'w', '-1':'s', '10':'d', '-10':'a'}
    str_numLog = list(map(str,numLog))
    
    for idx, value in enumerate(numLog):
        
        # idx 가 0 인 경우 예외처리.
        if idx == 0:
            continue
            
        # 1) idx, idx-1 값 계산
        # 2) 결과값을 num_position (dict) 의 key 값으로 사용
        # 3) 결과값 누적
        answer += num_position[str(numLog[idx] - numLog[idx-1])]
        
    return answer
        
        
