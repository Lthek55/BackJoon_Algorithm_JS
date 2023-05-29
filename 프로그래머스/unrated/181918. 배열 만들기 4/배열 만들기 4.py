def solution(arr):
    i = 0
    stk = []
    arrLen = len(arr)
    
    while arrLen > i:
        if not stk:
            stk.append(arr[i])
            i += 1
            continue
            
            
        if stk[-1] < arr[i]:

            stk.append(arr[i])
            i += 1
        elif stk[-1] >= arr[i]:
            stk.pop()
            
    return stk