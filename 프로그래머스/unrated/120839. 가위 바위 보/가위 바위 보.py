def solution(rsp):
    answer = ""
    for i in rsp:
        if "2" == i:
            answer += "0"
        elif "0" == i:
            answer += "5"
        else: 
            answer += "2"
    return answer        
