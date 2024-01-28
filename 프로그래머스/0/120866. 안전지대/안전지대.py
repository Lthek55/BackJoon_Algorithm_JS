def solution(board):
    bombEffect = [[0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1]]
    xLen = len(board[0])
    yLen = len(board)
    
    pivot = [[0 for i in range(xLen)] for j in range(yLen)]
    
    for i in range(yLen):
        for j in range(xLen):
            # 폭탄 발견
            if board[i][j] == 1: 
                pivot[i][j] = 1
                
                # print(f'i,j {i,j}')
                for effect in bombEffect: 
                    effectX = j + effect[0]
                    effectY = i + effect[1]
                    
                    
                    if 0<= effectX < xLen and 0<= effectY <yLen:
                        # print(effectX, effectY)
                        pivot[effectY][effectX] = 1
                        
    answer = 0
    for k in pivot:
        answer += k.count(0)
    return answer