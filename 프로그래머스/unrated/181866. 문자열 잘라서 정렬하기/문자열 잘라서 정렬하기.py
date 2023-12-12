def solution(myString):
    return sorted(filter(lambda x: x!='', myString.split('x')))