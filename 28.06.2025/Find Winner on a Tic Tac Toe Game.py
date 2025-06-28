class Solution(object):
    def tictactoe(self, moves):

        row = [0] * 3   
        col = [0] * 3   
        diag1 = 0        
        diag2 = 0        

        for move_number in range(len(moves)):
            rowIndex = moves[move_number][0]
            colIndex = moves[move_number][1]
            player = 1 if move_number % 2 == 0 else -1

            row[rowIndex] += player
            col[colIndex] += player
            
            if rowIndex == colIndex:
                diag1 += player
            
            if rowIndex + colIndex == 2:
                diag2 += player
        
            if (abs(row[rowIndex]) == 3 or 
                abs(col[colIndex]) == 3 or 
                abs(diag1) == 3 or        
                abs(diag2) == 3):          
                return 'A' if player == 1 else 'B'  
        
        return 'Draw' if len(moves) == 9 else 'Pending'
