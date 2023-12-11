def func(i):
    if i >= 50 and i % 2 == 0:
        return i // 2
    elif i < 50 and i % 2 == 1:
        return i * 2 + 1
    else:
        return i
    
def solution(arr):
    pre_arr = arr
    cnt = 0
    
    while True:
        new_arr = list(map(func, pre_arr))
        
        if pre_arr == new_arr:
            return cnt
        
        pre_arr = new_arr
        cnt += 1
        