################################
# Author: Keidy Lopez
# Filename: problem #4.py
# Description: calculates gross pay depending on whether or not that person worked 40 hrs or more
################################

def main():
    # gets input from user
    money = float(input("What is your hourly wage? "))
    hrs = float(input("How many hours did you work? "))

    # determines whether they worked over 40 hrs or not and displays proper gross pay
    if hrs > 40:
        print("Your gross pay for the week is:", OverWeekWage(money, hrs))
    elif hrs <= 40:
        print("Your gross pay for the week is:,", WeekWage(money, hrs))

# calculates pay if less than or equal to 40
def WeekWage(M, H):
    ans1 = M * H
    round(ans1, 2)
    return ans1

# calculates pay if more than 40
def OverWeekWage(M, H):
    ans1 = M * 40
    ans2 = ((1.5 * (H - 40)) * M)
    ans3 = ans1 + ans2
    round(ans3, 2)
    return ans3


if __name__ == "__main__":
    main()