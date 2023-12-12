def solution(arr, flag):
    ans = []
    for idx,v in enumerate(arr):
        if flag[idx] == True:
            ans += str(v) * (v*2) 
        else:
            del ans[-v:]        
    return list(map(int,ans))