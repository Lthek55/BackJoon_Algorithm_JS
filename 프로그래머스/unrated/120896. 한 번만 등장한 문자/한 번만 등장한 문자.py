from collections import Counter
def solution(s):
    pivot = Counter(s)
    ans = ""
    
    for k,v in pivot.items():    
        if v < 2: 
            ans += k
        
    return ''.join(sorted(ans))