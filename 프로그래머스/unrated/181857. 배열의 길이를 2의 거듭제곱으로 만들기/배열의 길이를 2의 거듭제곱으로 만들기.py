def solution(arr):

    # 1. math 모듈의 sqrt 를 사용하여 값이 2인 경우 그대로 반환
    # 1.2 1의 결과값이 2가 아닌 경우 예외처리 로직 실행
    # 1.A (반려사유) [2/4/8/16] 에 sqrt 함수를 사용하는 경우 [`2/2/2`2/4`/2] ( ` 는 루트를 의미 ) 로 값이 떨어지기에 판단하기 부적합.
    
    # 2. [2/4/8/16/32/64/128/256/512/1024] > 9개 
    # 2.1 len(arr) 와 pivot 을 비교하여, 동일할 경우 그대로 반환하고 차이값이 존재하는 경우 pivot[n] 과 len(arr) 의 차이 만큼 0 을 배열에 추가한다.
    # 2.2 len(arr) 가 1일 경우에 대한 조건은 없으므로 제외한다.
    # 2.2.A (반려사유) 2^0 == 1
    
    n = len(arr)
    ans = arr
    pivot = [2,4,8,16,32,64,128,256,512,1024]
    
    for idx, v in enumerate(pivot):
        if n == 1:
            return ans
        elif n == v: 
            return ans
        elif v > n: # n != v
            zero_arr = [0] * (pivot[idx] - n)
            ans += zero_arr
            return ans
            
    