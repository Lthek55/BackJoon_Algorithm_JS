from fractions import Fraction

def solution(a, b):
    f = Fraction(a,b)
    deno = f.denominator
    i = 2
    
    while deno > 1:
        if deno % i == 0:
            deno //= i
            if i != 2 and i != 5:
                return 2
        else:
            i+=1
    
        
    return 1