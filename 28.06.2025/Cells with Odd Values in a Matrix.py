class Solution(object):
    def oddCells(self, m, n, indices):
        row_arr = [0]*m
        col_arr = [0]*n
        count = 0
        for x in indices:
            row_arr[x[0]] += 1
            col_arr[x[1]] += 1
        for i in range(m):
            for j in range(n):
                if (row_arr[i] + col_arr[j]) %2 != 0:
                    count += 1
        return count
