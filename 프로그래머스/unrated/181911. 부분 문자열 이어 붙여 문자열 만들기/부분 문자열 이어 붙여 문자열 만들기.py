def solution(my_strings, parts):
    answer = ""
    n = len(my_strings)
    
    for idx in range(n):
        i,j = parts[idx]
        answer += my_strings[idx][i:j+1]
    return answer