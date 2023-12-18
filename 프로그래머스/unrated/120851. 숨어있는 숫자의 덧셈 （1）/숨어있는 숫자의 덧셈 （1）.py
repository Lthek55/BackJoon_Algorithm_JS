import string

def solution(my_string):
    pivot = list(string.ascii_lowercase)
    return sum([int(i) for i in my_string.lower() if i not in pivot])
