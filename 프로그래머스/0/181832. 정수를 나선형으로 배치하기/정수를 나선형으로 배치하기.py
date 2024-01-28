def solution(n):
    limit = n
    startPosition = "right"
    positionX = 0
    positionY = 0
    
    pivot = [[0 for i in range(n)] for j in range(n)]
    
    
    for i in range(1, n*n+1):
        pivot[positionX][positionY] = i 
        
        if startPosition == "right":
            if positionY + 1 == limit or pivot[positionX][positionY + 1] != 0:
                # 아래쪽으로 한칸 이동
                startPosition = "down"
                positionX += 1
            else: 
                positionY += 1 # 오른쪽으로 한칸 이동
                
        elif startPosition == "down":
            if positionX + 1 == limit or pivot[positionX + 1][positionY] != 0:
                startPosition = "left"
                positionY -= 1
            else: 
                positionX += 1
                
        elif startPosition == "left":
            if pivot[positionX][positionY - 1] != 0:
                startPosition = "up"
                positionX -= 1
            else: 
                positionY -= 1
                
        elif startPosition == "up":
            if pivot[positionX - 1][positionY] != 0:
                startPosition = "right"
                positionY += 1
            else: 
                positionX -= 1        
                
    return pivot
    
