class Solution:
    def shiftGrid(self, grid, k):
        rows = len(grid)
        cols = len(grid[0])
        modulo = rows * cols
        k = k % modulo
        
        if k == 0:
            return grid

        def swap_values(idx1, idx2):
            row1 = idx1 // cols
            col1 = idx1 % cols
            row2 = idx2 // cols
            col2 = idx2 % cols
            grid[row1][col1], grid[row2][col2] = grid[row2][col2], grid[row1][col1]

        idx = 0
        new_idx = idx
        elements_in_their_place = 0
        
        while elements_in_their_place < (modulo - 1):
            new_idx = (new_idx + k) % modulo
            
            if idx == new_idx:
                idx += 1
                new_idx = idx
                elements_in_their_place += 1
                continue
            
            swap_values(idx, new_idx)
            elements_in_their_place += 1
        
        return grid
