def solution(my_string, num1, num2):
    ans = ""
    for idx, v in enumerate(my_string):
        if idx == num1:
            ans += my_string[num2]
            continue
        elif idx == num2: 
            ans += my_string[num1]
            continue
        else: 
            ans += v
            
    return ans