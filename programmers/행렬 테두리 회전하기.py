def solution(rows, columns, queries):
    answer = []
    board = [[0 for i in range(columns+1)] for j in range(rows+1) ] 
    
    count=1
    for i in range(1,rows+1) :
        for j in range(1,columns+1) :
            board[i][j] = count
            count+=1

    for querie in queries :

        left_top = board[querie[0]][querie[1]]
        left_bottom = board[querie[2]][querie[1]]
        right_top = board[querie[0]][querie[3]]
        right_bottom = board[querie[2]][querie[3]]
        
        minVal = float('inf')
        for i in range(querie[3],querie[1],-1):
            if i == querie[1]+1 :
                board[querie[0]][i] = left_top
                minVal = min(minVal,left_top)
            else:
                board[querie[0]][i] = board[querie[0]][i-1]
                minVal = min(minVal,board[querie[0]][i])
        
        for i in range(querie[2],querie[0],-1) :
            if i == querie[0]+1 :
                board[i][querie[3]] = right_top
                minVal = min(minVal,right_top)
            else :
                board[i][querie[3]] = board[i-1][querie[3]]
                minVal = min(minVal,board[i][querie[3]])
        for i in range(querie[1],querie[3]) :
            if i == querie[3]-1 :
                board[querie[2]][i] = right_bottom
                minVal = min(minVal,right_bottom)
            else :
                board[querie[2]][i] = board[querie[2]][i+1]
                minVal = min(minVal,board[querie[2]][i])
        for i in range(querie[0],querie[2]) :
            if i == querie[2]-1 :
                board[i][querie[1]] = left_bottom
                minVal = min(minVal,left_bottom)
            else :
                board[i][querie[1]] = board[i+1][querie[1]]
                minVal = min(minVal,board[i][querie[1]])
        
        answer.append(minVal)

    return answer
