def solution(str_list):
    if "l" not in str_list and "r" not in str_list:
        return []

    for idx, v in enumerate(str_list):
        if v == "l":
            return str_list[:idx]
        elif v == "r":
            return str_list[idx+1:]
            
