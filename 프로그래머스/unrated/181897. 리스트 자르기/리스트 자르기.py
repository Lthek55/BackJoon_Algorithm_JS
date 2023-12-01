def solution(n, slicer, num_list):
    if 1== n:
        return num_list[:slicer[1]+1]
    elif 2== n:
        return num_list[slicer[0]:]
    elif 3== n:
        return num_list[slicer[0]:slicer[1]+1]
    else:
        return num_list[slicer[0]:slicer[1]+1:slicer[2]]