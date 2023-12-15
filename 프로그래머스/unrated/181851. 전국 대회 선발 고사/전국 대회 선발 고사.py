def solution(rank, attendance):
    pivot = {}
    for idx, v in enumerate(rank):
        if attendance[idx]: 
            pivot[v] = idx
    
    sorted_rank = dict(sorted(pivot.items(), key= lambda x : x[0]))
    sorted_rank_idx = list(sorted_rank.values())
    a,b,c = sorted_rank_idx[0], sorted_rank_idx[1], sorted_rank_idx[2]
    
    return 10000 * a + 100 * b + c