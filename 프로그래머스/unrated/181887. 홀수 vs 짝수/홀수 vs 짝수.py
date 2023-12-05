def solution(num_list):
    n = sum(num_list[::2])  # 짝수
    m = sum(num_list[1::2]) # 홀수 
    return n if n >= m else m