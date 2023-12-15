def solution(arr1, arr2):
    n,m = len(arr1), len(arr2)
    k,j = sum(arr1), sum(arr2)
    print(k,j)
    
    if n == m: 
        if k > j:
            return 1
        elif k < j:
            return -1
        else:
            return 0
    
    return 1 if n > m else -1