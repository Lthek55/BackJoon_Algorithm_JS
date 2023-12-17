def solution(my_string):
    pivot = {}
    ans = ''
    for i in my_string:
        if None == pivot.get(i):
            pivot[i] = i
            ans+=i
            
        else:
            continue
            
    return ans