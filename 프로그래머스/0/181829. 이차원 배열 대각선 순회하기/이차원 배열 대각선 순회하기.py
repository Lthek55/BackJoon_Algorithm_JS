def solution(board, k):
    rows = len(board)
    cols = len(board[0])
    answer = 0

    for i in range(rows):
        for j in range(cols):
            if i + j <= k: 
                answer += board[i][j]
    return answer