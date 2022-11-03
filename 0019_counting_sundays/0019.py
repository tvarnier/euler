class date:
    day = 1
    month = 1
    year = 1900

    def __init__(self, day = 1, month = 1, year = 1900):
        self.day = day
        self.month = month
        self.year = year

    def next(self):
        self.day += 1
        if (self.day == 29 and self.month == 2 and (self.year % 4 != 0 or (self.year % 100 == 0 and self.year % 400 != 0))) or (self.day == 30 and self.month == 2) or (self.day == 31 and self.month in [4, 6, 9, 11]) or self.day == 32:
            self.month += 1
            self.day = 1
        if self.month > 12:
            self.year += 1
            self.month = 1

    def __eq__(self, other):
        return (self.day == other.day and self.month == other.month and self.year == other.year)
    
    def __ne__(self, other):
        return (not(self == other))

def counting_sundays(begin, end):
    count = 0
    day_of_the_week = 1
    d = date(1, 1, 1900)
    while d != end:
        if d.year >= 1901 and d.day == 1 and day_of_the_week == 7:
            count += 1
        d.next()
        day_of_the_week = day_of_the_week + 1 if day_of_the_week < 7 else 1
    return count

if __name__ == '__main__':
    print(counting_sundays(date(1, 1, 1901), date(31, 12, 2000)))