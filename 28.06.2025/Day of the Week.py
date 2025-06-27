class Solution(object):
    def dayOfTheWeek(self, day, month, year):

        DayOfWeek = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        if month == 1 or month == 2:
            month += 12
            year -= 1

        year_of_century = year % 100
        century = year // 100
        decade = month

        weekday = (day + 13*(decade + 1) // 5 + year_of_century + year_of_century // 4 + century // 4 + 5 * century) % 7

        return DayOfWeek[weekday]
