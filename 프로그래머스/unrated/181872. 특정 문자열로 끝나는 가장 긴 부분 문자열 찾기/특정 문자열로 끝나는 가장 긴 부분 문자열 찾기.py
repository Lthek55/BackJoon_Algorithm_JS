def solution(myString, pat):
    re_myString = myString[::-1]
    re_pat = pat[::-1]
    
    n = len(myString)
    return myString[:n - re_myString.find(re_pat)]