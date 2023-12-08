def solution(score):
    pivot_arr = [i+j for i,j in score]
    
    pivot_score_idx = 0
    pivot_score = 0
    
    mapping_dict = {}
    
    
    for idx, v in enumerate(sorted(pivot_arr,reverse=True), start=1):
        
        if v == pivot_score:
            mapping_dict[v] = pivot_score_idx
            continue
            
        pivot_score_idx = idx
        pivot_score = v
        
        mapping_dict[v] = idx

    answer = []

    for i in pivot_arr: 
        answer.append(mapping_dict.get(i))
    
    return answer