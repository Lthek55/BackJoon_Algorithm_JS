def solution(polynomial):
    pivot = 0
    const = 0
    for i in polynomial.split(' + '):
        if i.isnumeric():
            const += int(i)
        else:
            if i == 'x':
                pivot += 1
            else: 
                pivot += int(i.replace('x',''))
    
    if pivot == 1:
        if const != 0: 
            return f"x + {const}"
        else: 
            return f"x"
    
    if const == 0:
        return f"{pivot}x"
    if pivot == 0 :
        return f"{const}"
    
    
    return f"{pivot}x + {const}"