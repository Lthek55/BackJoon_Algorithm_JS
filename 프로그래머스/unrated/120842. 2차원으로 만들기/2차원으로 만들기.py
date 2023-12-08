def solution(num_list, n):
    answer = []
    pivot_arr = []
    for idx,v in enumerate(num_list,start=1):
        pivot_arr.append(v)
        if 0 == idx % n:
            answer.append(pivot_arr)    
            pivot_arr = []
    return answer