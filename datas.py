from datetime import timedelta,time,datetime,date

class MyDate:
    def __init__(self,day,month,year) -> None:
        self.day = day
        self.month = month
        self.year = year
        self.MONTHS = ["Yanvar","Fevral","Mart",'Aprel',"May","Iyun","Iyul","Avgust","Sentabr","Oktabr","Noyabr","Dekabr"]
        self.DAY_IN_MONTHS  = [31,28,31,30,31,30,31,31,30,31,30,31]

    def __str__(self) -> str:
        return f"""{self.day}-{self.MONTHS[self.month-1]} {self.year} yil"""
    
    def isLeapYear(self,year):
        self.year = year
        if (self.year % 4 == 0 and self.year % 100 != 0) or self.year%400 == 0:
            return True
        return False
    def isValidDate(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year
        if 1 <= self.year <= 9999 and 1 <= self.month <= 12 and 1 <= self.day <= 31:
            return True
        return False
    def setDate(self,day,month,year):
        if self.isValidDate(self.day,self.month,self.year):
            self.day = day
            self.month = month
            self.year = year
            return f"{self.day}.{self.month}.{self.year}"
        else:
            return "Yil,oy yoki kun noto'g'ri kiritilgan!"
    
    def setYear(self,new_year):
        if  1 <= new_year <= 9999:
            self.new_year = new_year
        else:
            return "Yil noto'g'ri"
 
    def setMonth(self,new_month):
        if 1 <= new_month <= 12:
            self.new_month= new_month
        else:
            return "Oy hato kiritildi"

    def setDay(self,new_day):
        if 1 <= new_day <= 31:
            self.new_day= new_day
        else:
            return "Oy hato kiritildi"

    def getYear(self):
        return self.year
    
    def getMonth(self):
        return self.month

    def getDay(self):
        return self.day
    
    def nextDay(self):
        # cur_date = date(self.year, self.month, self.day)
        # next_day = cur_date + timedelta(days=1)
        # return next_day
        if self.month == 2 and self.isLeapYear(self.year):
            if self.day < 29:
                self.day += 1
            else:
                self.day = 1
                self.month += 1
        elif self.day == 31:
            if self.month == 12:
                self.year += 1
                self.month = 1
            else:
                self.month += 1
            self.day = 1
        else:
            self.day += 1
        return self.day, self.month, self.year
    
    def nextMonth(self):
        if self.month == 12:
            self.year += 1
            self.month = 1
        else:
            self.month += 1
        return self.month
    def nextYear(self):
        self.year += 1
        return self.year
           
    def previousDay(self):
        date1 = date(self.day,self.month,self.year)
        previous_Day = date1 + timedelta(days=-1)
        return previous_Day 

    def previous_month(self):
        if self.month == 1:
            self.year -= 1
            self.month = 12
        else:
            self.month -= 1

    def previous_year(self):
        self.year -= 1
        
mydate = MyDate(28,2,2012)
print(mydate)
mydate.nextDay()
print(mydate)
mydate.nextDay()
mydate.nextMonth()
print(mydate)
mydate.nextYear()
print(mydate)

