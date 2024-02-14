################################
# Author: Keidy Lopez
# Filename: problem #6.py
# Description: program that tell you how much x amount of seconds is in days hours minutes and the remaining seconds
################################

def main():
    # asks for seconds input
    sec = int(input("Please enter a number of seconds: "))

    # determines what function/s to use depending on how big the number entered is
    if sec < 60:
        print(sec, "seconds is", sec, "seconds")
    elif 60 < sec < 3600:
        print(sec, "seconds is", SecToMin(sec), "minute(s) and", DayHrMinSec(sec), "seconds")
    elif 3600 < sec < 86400:
        print(sec, "seconds is", SecToHr(sec), "hour(s),", DayHrMin(sec), "minute(s) and", DayHrMinSec(sec), "seconds")
    elif sec >= 86400:
        print(sec, "seconds is", SecToDay(sec), "day(s)", DayHr(sec), "hour(s),", DayHrMin(sec),"minute(s) and", DayHrMinSec(sec), "seconds")

# calculates seconds into minutes
def SecToMin(S):
    min = S // 60
    return min

# calculates seconds into hours
def SecToHr(S):
    hr = S // 3600
    return hr

# calculates seconds into days
def SecToDay(S):
    day = S // 86400
    round(day , 1)
    return day

# Got some help from Eliza, calculates remaining number of seconds
def DayHrMinSec(S):
    rem1 = S % 86400
    rem2 = rem1 % 3600
    rem3 = rem2 % 60
    return rem3

# calculates remaining number of minutes
def DayHrMin(S):
    rem1 = S % 86400
    rem2 = rem1 % 3600
    rem3 = rem2 // 60
    return rem3

# calculates remaining number of hours
def DayHr(S):
    rem1 = S % 86400
    rem2 = rem1 // 3600
    return rem2


if __name__ == "__main__":
    main()
