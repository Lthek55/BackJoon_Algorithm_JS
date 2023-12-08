def solution(lines):
    pivot_arr = [0] * 201
    for i,j in lines:
        for n in range(i,j):
            pivot_arr[n+100] += 1
    answer = 0
    for m in pivot_arr:
        if m >=2: 
            answer +=1
    return answer