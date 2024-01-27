import string
def solution(my_string):
    alphabet = string.ascii_lowercase+string.ascii_uppercase
    zero = '_'* 52
    pivotTable = str.maketrans(alphabet, zero)
    
    transResult = list(filter(lambda x : x!= '', my_string.translate(pivotTable).split('_')))
    answer = list(map(int,transResult))
    
    return sum(answer)