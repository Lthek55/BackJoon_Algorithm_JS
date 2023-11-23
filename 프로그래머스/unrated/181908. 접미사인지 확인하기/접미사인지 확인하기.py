def solution(my_string, is_suffix):
    pivot_arr = []
    
    for idx in range(len(my_string)):
        pivot_arr.append(my_string[idx:])
        
    is_answer = pivot_arr.count(is_suffix)
    return is_answer