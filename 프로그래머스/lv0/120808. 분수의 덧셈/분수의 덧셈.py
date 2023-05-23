from math import gcd

def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    # LCM ( 최소 공배수 ) 
    # denom 이 2,3 인 경우 LCM 값인 6까지 loop 를 돌지 못하여 값을 구하지 못하는 상황 방지하기 위해 +1 추가
    for i in range(min(denom1, denom2), (denom1 * denom2 + 1)): 
        # print("i",i)
        if i % denom1 ==0 and i % denom2==0:
            # print("LCM 찾음")

            result_numer = numer1 * (i//denom1) + numer2 * (i//denom2)
            result_denom = i
            
            # 기약 분수 계산, 최대 공약수 
            # print("gcd(result_numer,result_denom)",gcd(result_numer,result_denom))
            gcd_value = gcd(result_numer,result_denom)
            
        
            answer.append(result_numer//gcd_value) 
            answer.append(result_denom//gcd_value)
            
            # print("result_numer",result_numer)
            # print("result_denom",result_denom)
            break
    
    return answer
