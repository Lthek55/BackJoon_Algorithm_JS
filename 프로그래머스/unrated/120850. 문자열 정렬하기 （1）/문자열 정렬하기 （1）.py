def solution(my_string):
    pivot_int_arr = list(range(10))
    return sorted([int(i) for i in my_string if i.isdigit() and int(i) in pivot_int_arr])