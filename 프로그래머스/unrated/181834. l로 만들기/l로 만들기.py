import string
def solution(myString):
    lower_arr = list(string.ascii_lowercase)
    pivot_lower_arr = lower_arr[:lower_arr.index('l')]
    
    return ''.join([i if i not in pivot_lower_arr else 'l' for i in myString])
    
