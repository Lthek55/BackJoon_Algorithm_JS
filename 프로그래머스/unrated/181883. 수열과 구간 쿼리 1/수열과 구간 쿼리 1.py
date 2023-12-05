def solution(arr, queries):
    for i,j in queries:
        for n in range(i, j+1):
            arr[n] +=1
    return arr            