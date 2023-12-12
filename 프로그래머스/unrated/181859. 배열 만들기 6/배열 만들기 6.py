def solution(arr):
    i = 0
    stk = []
    
    # [0, 1, 0, 0]
    # 0 > stk 0
    # 1 > stk 0, 1
    # 2 > stk 0, 1 ,0
    # 3 > stk 0,1
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i+=1
        
        elif len(stk) != 0 and stk[-1] == arr[i]:
            stk.pop()            
            i+=1
        
        elif len(stk) != 0 and stk[-1] != arr[i]:
            stk.append(arr[i])
            i+=1
            
    return [-1] if len(stk) == 0 else stk
            