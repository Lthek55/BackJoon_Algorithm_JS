def solution(arr, queries):
    # 1) queries 순회
    # 2) for .. loop > query 시작
    # 3) query[0] : s, query[1] : e , query[2] : k , s ~ e 사이값 : i
    # 4) s < i < e 조건 처리 및 arr 값 누적
    # 5) for .. loop > query 종료
    # 6) 1번으로 돌아가 더 이상 순회할 queries 가 없을때가지 반복.
    
    for query in queries:
        # print("arr",arr) idx = 0~ 로그 출력용
        for i in range(query[0], query[1] + 1):
            if i % query[2] == 0:
                arr[i]+=1
                
    # print("arr",arr) idx = -1 로그 출력용                
    return arr
        
            
