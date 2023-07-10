def solution(intStrs, k, s, l):
    answer = []
    
    for i in intStrs:
        # 배열의 문자열 추출
        pivot = int(i[s:s+l])
        
        # 값 비교
        if int(pivot) > k:
            answer.append(pivot)
        
    return answer
    



    
