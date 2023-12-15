def solution(arr, k):
    # 배열 중복 제거
    ans  = list(dict.fromkeys(arr))
    
    n = len(ans)
    
    # 배열 길이와 k 값 비교 
    if k > n: 
        # 횟수 반복
        for _ in range(k-n):
            ans.append(-1)
        return ans
    
    
    # 결과값 출력 
    return ans[:k]
