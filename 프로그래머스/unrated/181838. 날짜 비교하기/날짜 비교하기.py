def solution(date1, date2):
    # 1,0,-3 > 1
    # 0,0,2 > 1 ( error point )
    # 0,0,0 > 0 
    # -3,0,0 > 0
    # -3,1,2 > 0
    pivot = 0
    for idx, date in enumerate(date2):
        # 1,0,-3 > 1
        if date1[idx] < date: 
            return 1
        
        # 0,0,2
        if date1[idx] == date: 
            pivot += 1
        
        # -3,-3,2 
        if date1[idx] > date: 
            return 0 
            
    if pivot >= 2 and date1[2] < date2[2]: 
        return 1
    return 0