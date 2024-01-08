#from pypdf import PdfReader
#import mdpdf

SEPERATOR = '.'
DATE_FORMAT = "YYYY.MM.DD" # Input Date Format (4 Ys)
FORMAT = '.md' # You did read the description of this repo, did you? It should always be '.md'

DAY_DICT = {1:31, 3:31, 4:30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10:31, 11: 30, 12: 31}
DATE_FORMAT = DATE_FORMAT.split(SEPERATOR)
for i in range(0, 3):
    if DATE_FORMAT[i] == 'YYYY':
        YEAR_SLOT = i
    elif DATE_FORMAT[i] == 'MM':
        MONTH_SLOT = i
    elif DATE_FORMAT[i] == 'DD':
        DAY_SLOT = i
    else:
        raise ValueError("Seems like your date format is wrong.")

def TwentyNinthFeb(year: int):
    # returns true if the given year is a leap year
    if year % 100 == 0:
        if year % 400 == 0: return True
        else: return False
    elif year % 4 == 0:
        return True
    else: return False

def initDate(date: str):
    # takes a date string and converts it into a list of ints
    date = date.split(SEPERATOR)
    date = list(map(int, date))
    if validateDate(date):
        return date
    else:
        raise ValueError("invalid date")

def validateDate(date: list):
    # returns True if the given date is valid
    # returns False if the give date is invalid
    if 1 <= date[MONTH_SLOT] <= 12:
        if date[MONTH_SLOT] == 2:
            if date[DAY_SLOT] == 29:
                if TwentyNinthFeb(date[YEAR_SLOT]): return True
                else: return False

            elif 0 < date[DAY_SLOT] < 29: return True
            else: return False

        else:
            if date[DAY_SLOT] <= DAY_DICT[date[MONTH_SLOT]]: return True
            else: return False
    else: return False

def dateBeforeDate(date1: list, date2: list):
    # returns True if date1 is the same as or a date before date2
    # assumes the dates have been init-ed and use the pre-definied date format
    if date1 == date2: return True

    if date1[YEAR_SLOT] < date2[YEAR_SLOT]: return True

    elif date1[YEAR_SLOT] == date2[YEAR_SLOT]:
        if date1[MONTH_SLOT] < date2[MONTH_SLOT]: return True
        
        elif date1[MONTH_SLOT] == date2[MONTH_SLOT]:
            if date1[DAY_SLOT] < date2[DAY_SLOT]: return True
            
            else: return False

        else: return False

    else: return False

def addOneDay(date: list):
    # returns the given date with one day added
    date[DAY_SLOT] += 1
    if validateDate(date): return date
    else:
        date[DAY_SLOT] = 1
        date[MONTH_SLOT] += 1
        if validateDate(date): return date
        else:
            date[MONTH_SLOT] = 1
            date[YEAR_SLOT] += 1
            if validateDate(date): return date
            else: raise ValueError("I don't see any scenario where this error is raised. Have you validated your day before trying to add one day?")

def toTwoDigit(number):
    # converts a number (might be a string or an int) of length 0 into a string of length 2 by prepending zeroes and returns it
    # returns the string if it's already 2 or more digits long
    number = str(number)
    digits = len(number)
    if digits >= 2:
        return number
    elif digits == 1:
        return "0" + number
    else:
        raise ValueError("Sorry, only numbers with length one or above allowed")
def toFourDigit(number):
    # converts a number (might be a string or an int) of length 0 into a string of length 2 by prepending zeroes and returns it
    # returns the string if it's already 2 or more digits long
    number = str(number)
    digits = len(number)
    if digits >= 4:
        return number
    elif digits == 1:
        return "000" + number
    elif digits == 2:
        return "00" + number
    elif digits == 3:
        return "0" + number
    else:
        raise ValueError("Sorry, only numbers with length one or above allowed")

def makePrintable(date: list):
        date[DAY_SLOT] = toTwoDigit(date[DAY_SLOT])
        date[MONTH_SLOT] = toTwoDigit(date[MONTH_SLOT])
        date[YEAR_SLOT] = toFourDigit(date[YEAR_SLOT])
        return date[0] + SEPERATOR + date[1] + SEPERATOR + date[2] + FORMAT


if __name__ == "__main__":
    startDate = input("Start Date: ")
    startDate = initDate(startDate)

    endDate = input("End Date: ")
    endDate = initDate(endDate)

    if dateBeforeDate(startDate, endDate):
        print(makePrintable(startDate.copy()))
        while startDate != endDate:
            startDate = addOneDay(startDate)
            print(makePrintable(startDate.copy()))
    else: raise ValueError("The start date is after the end date.")