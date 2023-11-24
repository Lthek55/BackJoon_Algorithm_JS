def solution(my_string):
    pivot = []
    for i in range(len(my_string)):
        pivot.append(my_string[i:])
    pivot.sort()
    return pivot