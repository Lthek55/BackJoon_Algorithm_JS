def solution(emergency):
    sorted_emergency = sorted(emergency,reverse=True)
    pivot_dict = {}
        
    for idx, v in enumerate(sorted_emergency,start=1):
        pivot_dict[v] = idx

    answer = []
    for j in emergency:
        answer.append(pivot_dict[j])
    return answer