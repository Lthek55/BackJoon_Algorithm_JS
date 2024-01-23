def solution(numbers):
    pivot = sorted(list(numbers))
    answer = -100000000
    
    for i in range(len(pivot)): 
        for j in range(i+1, len(pivot)):
            result = pivot[i] * pivot[j]
            
            if result > answer:
                answer = result
                
    return answer
                
# [5,5] 인 경우 set() 사용하여 동일 원소를 없애면 안된다.
# [-10000, 1] 인 경우 체크를 위해 비교 값 기준을 -10001 로 해야한다.
# [-10000, 10000] 인 경우 나올 수 있는 최대값이 비교값 기준을 넘어간다.