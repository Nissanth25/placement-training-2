class Solution(object):
    def dayOfYear(self, date):
        d = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        year, month, day = date.split('-')
        
        total = 0
        for m in range(1, int(month)):
            if m == 2:
                if self.isLeap(int(year)): total += (d[m]+1)
                else: total += (d[m])
            else: total += d[m]
        total += int(day)
        return total 
        
    def isLeap(self, year):  
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
