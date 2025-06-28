class Solution(object):
    def luckyNumbers (self, matrix):

        maxRows, maxCols = len(matrix), len(matrix[0])
        maxRowList, maxColList = [[]] * maxRows, [[]] * maxCols
        maxRowItem, maxColumnItem = [-1] * maxRows, [-1] * maxCols
        ret = []
        for i in range(maxRows):
            thisMaxRow = float("inf")
            thisIndex = [-1, -1]
            for j in range(maxCols):
                cell = matrix[i][j]
                if cell < thisMaxRow:
                    thisMaxRow = cell
                    thisIndex = [i, j]
            maxRowList[i] = thisIndex
            maxRowItem[i] = thisMaxRow

        for i in range(maxRows):
            for j in range(maxCols):
                cell = matrix[i][j]
                if cell > maxColumnItem[j]:
                    maxColumnItem[j] = cell
                    maxColList[j] = [i, j]
        
        for item in maxColList:
            [row, col] = item
            if maxRowItem[row] == maxColumnItem[col]:
                ret.append(maxRowItem[row])
        
        return ret
