def solution(my_string):
    pivot_arr = ['a', 'e', 'i', 'o', 'u']
    return ''.join(list(filter(lambda x : x not in pivot_arr, my_string)))