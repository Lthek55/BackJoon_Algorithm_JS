def solution(arr):
    for idx, v in enumerate(arr): 
        if v >= 50 and v % 2 == 0 :
            arr[idx] /= 2
        elif v < 50 and v % 2 == 1 :
            arr[idx] *= 2
        else:
            continue
    return arr