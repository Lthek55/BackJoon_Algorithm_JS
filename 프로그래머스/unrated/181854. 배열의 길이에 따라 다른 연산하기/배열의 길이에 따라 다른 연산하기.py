def solution(arr, n):
    k = len(arr)
    ans = arr
    
    for i in range(k): 
        if k % 2 == 0:
            if (i+1) % 2 == 0:
                ans[i] += n 
        else: 
            if (i+1) % 2 != 0:
                ans[i] += n 
            
    return ans