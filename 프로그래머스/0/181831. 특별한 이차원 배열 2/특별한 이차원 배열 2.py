def solution(arr):
    row_len = len(arr)
    col_len = len(arr[0])
    
    for i in range(row_len):
        for j in range(col_len):
            if arr[i][j] != arr[j][i]:
                return 0
    
    return 1