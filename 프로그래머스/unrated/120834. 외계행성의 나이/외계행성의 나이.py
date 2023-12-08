import string

def solution(age):
    pivot_dict = {}
    for idx,v in enumerate(string.ascii_lowercase):
        pivot_dict[idx] = v

        
    answer = ""
    for i in str(age):
        answer += pivot_dict.get(int(i))
    return answer