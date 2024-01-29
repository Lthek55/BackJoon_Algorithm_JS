def solution(my_str, n):
    answer = []
    pivot = 0
    for i in range(n, len(my_str), n):
        answer.append(my_str[pivot:i])
        pivot = i
    
    answer.append(my_str[pivot:])
    return answer