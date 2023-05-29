def solution(arr, queries):
    arr_idx = 0
    # 1) quieries 순회
    # 2) 각 loop 의 query 값 확인. (idx > 0,1)
    # 3) idx 를 arr 에 대입 및 값 조회
    # 4) 값 교체 
    # 5) loop 종료
    # 6) 다시 1부터 순회가 종료될때까지 반복 진행
    
    for query in queries:
        
        pick = arr[query[0]]
        
        arr[query[0]] = arr[query[1]]
        arr[query[1]] = pick
        
    return arr