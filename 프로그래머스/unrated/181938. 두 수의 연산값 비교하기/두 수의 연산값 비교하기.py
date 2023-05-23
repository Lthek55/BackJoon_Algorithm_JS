def solution(a, b):
    n1 = int(f"{a}{b}")
    n2 = 2 * a * b
    
    if n1 == n2:
        return n1
    
    return n1 if n1 > n2 else n2
  