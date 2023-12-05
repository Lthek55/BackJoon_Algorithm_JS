def solution(arr, query):
    
    answer = arr
    
    for idx, q in enumerate(query):
        if 0 == idx % 2:
            answer = answer[:q+1]
        else:
            answer = answer[q:]
            
    return answer