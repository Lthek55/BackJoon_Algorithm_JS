
def solution(numlist, n):
    answer = []
    pivot_dict = {}
    
    
    for i in sorted(numlist, reverse=True):
        pivot_dict[i] = abs(n-i)
        
    pivot_sorted_dict = {k:v for k,v in sorted(pivot_dict.items(), key = lambda x: x[1])}
    
    return list(pivot_sorted_dict.keys())
