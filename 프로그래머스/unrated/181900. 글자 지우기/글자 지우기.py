def solution(my_string, indices):
    st = list(my_string)
    for i in indices:
        st[i] = '' 
    return ''.join(st)