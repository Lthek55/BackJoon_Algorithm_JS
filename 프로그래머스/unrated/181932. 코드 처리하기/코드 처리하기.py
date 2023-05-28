def solution(code):
    ret = ''
    mode = 0
    
    for idx, value in enumerate(code):
        if mode == 0:
            if code[idx] != '1': 
                ret = ret + (code[idx] if idx % 2 == 0 else "")
                #print("조건 1 실행됨")
                
            if code[idx] == '1':  
                mode = 1
                #print("조건 2 실행됨")
        
                
        elif mode == 1:
            if code[idx] != '1': 
                ret = ret + (code[idx] if idx % 2 != 0 else "")
                #print("조건 3 실행됨")
                
            if code[idx] == '1':  
                mode = 0
                #print("조건 4 실행됨")
                
        #print(idx, code[idx], mode, ret )
        
    return ret if ret else "EMPTY"