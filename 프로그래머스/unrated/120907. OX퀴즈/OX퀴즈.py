def solution(quiz):
    answer = []
    pivot_arr = [i.split(' ') for i in quiz]
    
    for j in pivot_arr: 
        if j[1] == '-':
            if int(j[0]) - int(j[2]) == int(j[4]):
                answer.append('O')
            else:
                answer.append('X')
        else: 
            if int(j[0]) + int(j[2]) == int(j[4]):
                answer.append('O')
            else:
                answer.append('X')
    return answer