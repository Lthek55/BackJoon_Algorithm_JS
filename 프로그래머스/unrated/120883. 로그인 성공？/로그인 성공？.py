def solution(id_pw, db):
    
    user_input_id = id_pw[0]
    user_input_pw = id_pw[1]
    
    db_id = []
    db_pw = []
    
    for idx in range(len(db)):
        
        db_id.append(db[idx][0])
        db_pw.append(db[idx][1])
    
    if user_input_id in db_id:
        if db_pw[db_id.index(user_input_id)] == user_input_pw :
            return "login"
        else:
            return "wrong pw"
    else: 
        return "fail"
        
