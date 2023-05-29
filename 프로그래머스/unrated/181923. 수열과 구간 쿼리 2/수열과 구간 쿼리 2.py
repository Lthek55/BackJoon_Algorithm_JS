import operator


def solution(arr, queries):
    # 1) queries 순회
    # 2) 각 query 의 0,1 인덱스의 사이값을 구한다.
    # 3) 구한 인덱스 값을 기반으로 arr 에서 값을 조회한다.
    # 4) query 의 2 인덱스값을 기준으로 앞서 3 에서 구한값을 필터링한다. 
    # 5) loop 를 종료한다.
    # 6) 1 로 돌아가 반복한다.
    
    answer = []
    pick_value = []
    
    for query in queries:
        for i in range(query[0],query[1]+1):
            
            if operator.gt(arr[i], query[2]):
                pick_value.append(arr[i])
                
        # 배열이 비었을 경우 -1 예외처리
        if not pick_value :
            pick_value.append(-1)
                
        # pick_value 가 비었을 경우의 예외처리 때문에 loop 에 answer 를 직접적으로 사용하지 못함.
        answer.append(min(pick_value))
        pick_value = []
        
    return answer
    
    
