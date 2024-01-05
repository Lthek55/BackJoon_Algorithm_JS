def solution(num, total):
    
    pivot_plus_arr = [i for i in range(1001)]
    pivot_minus_arr = [i for i in range(-100,0,1)]
    
    pivot_arr = pivot_minus_arr + pivot_plus_arr
    
    window = sum(pivot_arr[:num])
    answer = window
    
    for i in range(num, len(pivot_arr)):
        window += pivot_arr[i] - pivot_arr[i-num]
        
        answer = max(answer, window)
        
        if answer == total: 
            return pivot_arr[i-num+1:i+1]