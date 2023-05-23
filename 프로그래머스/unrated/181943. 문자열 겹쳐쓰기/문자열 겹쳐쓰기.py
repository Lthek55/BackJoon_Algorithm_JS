def solution(my_string, overwrite_string, s):
    overwrite_string_len = len(overwrite_string)
    
    w1 = my_string[:s]
    w2 = overwrite_string
    w3 = my_string[s+overwrite_string_len:]
    
    # print(f"{w1}{w2}{w3}")
    
    answer = f"{w1}{w2}{w3}"
    return answer

