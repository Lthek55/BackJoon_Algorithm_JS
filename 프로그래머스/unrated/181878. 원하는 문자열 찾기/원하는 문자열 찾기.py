
def solution(myString, pat):
    lower_myString = myString.lower()
    lower_pat = pat.lower()

    return 1 if lower_myString.find(lower_pat) >= 0 else 0
    
    