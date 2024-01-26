def solution(s):
    # ['1','z','2']
    # stack()
    # loop ['1','z','2']
    # stack(['1'])
    # 'z' 인 경우 stack.pop()
    
    pivot = s.split()
    stack = []
    
    for i in pivot: 
        if i != 'Z':
            stack.append(i)
        else: 

            stack.pop()
    return sum(map(int,stack))