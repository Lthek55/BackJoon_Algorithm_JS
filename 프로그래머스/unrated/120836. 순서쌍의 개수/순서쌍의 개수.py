def solution(n):
    pivot_arr = list(range(1, n+1))
    start = 0
    end = len(pivot_arr) -1
    answer = 0
    
    while start <= end:
        
        if n == pivot_arr[start] * pivot_arr[end]:
            answer += 1
            if pivot_arr[start] != pivot_arr[end]:
                answer += 1
        
        if pivot_arr[start] * pivot_arr[end] <= n:
            start +=1
        elif pivot_arr[start] * pivot_arr[end] > n:
            end -=1
        
    return answer