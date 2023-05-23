def solution(a, b):
    n1 = int(f"{a}{b}")
    n2 = int(f"{b}{a}")
    
    answer = n1 if n1 > n2 else n2
    return answer