def solution(a, b, c):
    arr = list(set([a,b,c]))
    arr_len = len(arr)
    
    if arr_len == 1 or arr_len == 2 or arr_len == 3:
        answer =  a + b + c
    if arr_len == 1 or arr_len == 2:
        answer = answer * (a**2 + b**2 + c**2)
    if arr_len == 1 :
        answer = answer * (a**3 + b**3 + c**3)
    
    return answer
