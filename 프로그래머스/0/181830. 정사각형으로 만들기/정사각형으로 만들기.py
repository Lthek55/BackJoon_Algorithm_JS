def solution(arr):
    rowLen = len(arr)
    colLen = len(arr[0])
    
    if rowLen > colLen:
        for row in arr:
            for i in range(rowLen-colLen):
                row.append(0)
        return arr
            
    elif rowLen < colLen:
        for i in range(colLen - rowLen):
            arr.append([0]* colLen)
        return arr
        
    else: 
        return arr
