def solution(arr, idx):
    for i in range(idx,len(arr)):
        if 1 == arr[i]:
            return i
    return -1