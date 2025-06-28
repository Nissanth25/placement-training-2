from datetime import datetime

class Solution(object):
    def daysBetweenDates(self, date1, date2):
        date1_obj = datetime.strptime(date1, "%Y-%m-%d")
        date2_obj = datetime.strptime(date2, "%Y-%m-%d")
        difference = abs((date2_obj - date1_obj).days)
        return difference
